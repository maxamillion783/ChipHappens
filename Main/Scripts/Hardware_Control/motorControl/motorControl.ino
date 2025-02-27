/*
This code was created by Cole Barton on 2/6/2025.
The purpose of this code is to control the hardware on CPI card group's
card counter. It will be the script that runs on the ATMEGA32U4, which is
the lattePanda's onboard microcontroller. 
*/

#include <AccelStepper.h>

// //Limit switch pins
// const byte LEFT_LIMIT_SWITCH_PIN = 11; //Limit switch on the left end of the rail
// const byte RIGHT_LIMIT_SWITCH_PIN = 12; //Limit switch on the right end of the rail
// const byte TRAY_POSITION_PIN = 13; //Switch to tell whether the tray is in position for a scan
// //Motor driver pins
// const byte ENABLE_PIN = 57; //LOW -> allow motion, HIGH -> block motion
// const byte STEP_PIN = 56;   //Rising signal -> step motor once
// const byte DIR_PIN = 55;    //LOW -> clockwise?, HIGH -> counterclockwise?

//Limit switch pins
const byte LEFT_LIMIT_SWITCH_PIN = 2; //Limit switch on the left end of the rail
const byte RIGHT_LIMIT_SWITCH_PIN = 3; //Limit switch on the right end of the rail
const byte TRAY_POSITION_PIN = 4; //Switch to tell whether the tray is in position for a scan
//Motor driver pins
const byte ENABLE_PIN = 8; //LOW -> allow motion, HIGH -> block motion
const byte STEP_PIN = 9;   //Rising signal -> step motor once
const byte DIR_PIN = 10;    //LOW -> clockwise?, HIGH -> counterclockwise?

// Define motor parameters
const float MAX_SPEED = 1500.0;   //[steps per second]
const float ACCELERATION = 1500.0; //[steps per second]
const float HOMING_SPEED = 500.0; //Slower speed for homing sequence [steps per second]

//Create a stepper motor object using 2-wire constructor
AccelStepper stepper(AccelStepper::FULL2WIRE, STEP_PIN, DIR_PIN);

// Variables
long stepsBetweenSwitches = 0; //Number of steps between limit switches
bool isHomed = false;          //State variable which tracks whether the motor has been homed

void setup() {
  //Set up inputs from switches
  pinMode(LEFT_LIMIT_SWITCH_PIN, INPUT_PULLUP);
  pinMode(RIGHT_LIMIT_SWITCH_PIN, INPUT_PULLUP);
  pinMode(TRAY_POSITION_PIN, INPUT_PULLUP);
  pinMode(LED_BUILTIN,OUTPUT);

  //Configure the stepper motor
  stepper.setMaxSpeed(MAX_SPEED);
  stepper.setAcceleration(ACCELERATION);
  stepper.setSpeed(HOMING_SPEED);
  digitalWrite(ENABLE_PIN,LOW);
  digitalWrite(DIR_PIN,HIGH);

  Serial.begin(9600);
}

void loop() {
  //Check for serial communication
  if (Serial.available() > 0) {
    char command = Serial.read();

    //If homing sequence is commanded and the tray is in position, run homing sequence
    if (command == 'H') {
      homeMotor();
      // if (digitalRead(TRAY_POSITION_PIN) == LOW){
      //   //Perform homing sequence
      //   homeMotor();
      // } else {
      //   //Serial.println("Error: Tray out of position.");
      //   Serial.println("0");
      // }
    }
    //If scan is commanded, the tray is in position, and it's already been homed, run scanning sequence
    else if (command == 'S') {
      if (isHomed) {
        if (digitalRead(TRAY_POSITION_PIN) == LOW) {
          //Perform scan sequence
          performScan();
        } else {
          //Serial.println("Error: Tray out of position.");
          Serial.println("0");
        }
      } else {
        //Serial.println("Error: Motor not homed. Perform homing first.");
        Serial.println("0");
      }
    }
  }
}

void homeMotor() {
  //Serial.println("Starting homing sequence...");

  //Move motor to the right until the right limit switch is pressed
  stepper.setSpeed(HOMING_SPEED);
  long startTime = millis();
  while (digitalRead((RIGHT_LIMIT_SWITCH_PIN) == HIGH) && (millis() - startTime < 10000)) {
    stepper.runSpeed();
    // if (digitalRead(TRAY_POSITION_PIN) == LOW){
    //   stepper.runSpeed();
    // } else {
    //   //Serial.println("Error: Tray out of position.");
    //   Serial.println("0");
    //   stepper.stop();
    //   return;
    // }
  }
  stepper.stop();
  stepper.setCurrentPosition(0); //Temporarily set the current position as 0

  //Move motor to the left until the left limit switch is pressed
  stepper.setSpeed(-HOMING_SPEED);
  startTime = millis();
  while ((digitalRead(LEFT_LIMIT_SWITCH_PIN) == HIGH) && (millis() - startTime < 10000)) {
    stepper.runSpeed();
    // if (digitalRead(TRAY_POSITION_PIN) == LOW){
    //   stepper.runSpeed();
    // } else {
    //   //Serial.println("Error: Tray out of position.");
    //   Serial.println("0");
    //   stepper.stop();
    //   return;
    // }
  }
  stepper.stop();

  // Calculate the number of steps between the switches
  stepsBetweenSwitches = -stepper.currentPosition();
  stepper.setCurrentPosition(0); //Set the current position as 0

  //Serial.println("Homing complete. Steps between switches: " + String(stepsBetweenSwitches));
  isHomed = true;

  Serial.println("1");
}

void performScan() {
  Serial.println("Starting scan sequence...");

  //Move the carriage to the right end. Sensor should be gathering data by this point.
  stepper.moveTo(stepsBetweenSwitches);
  long startTime = millis();
  while (stepper.distanceToGo() != 0 && (millis() - startTime < 10000)) {
    stepper.run();
    //Check if either limit switch is pressed after each step
    if (digitalRead(LEFT_LIMIT_SWITCH_PIN) == LOW || digitalRead(RIGHT_LIMIT_SWITCH_PIN) == LOW) {
      //Serial.println("Scan unsuccessful: Limit switch triggered.");
      Serial.println("0");
      stepper.stop();
      isHomed = false;
      return;
    } else if (digitalRead(TRAY_POSITION_PIN) == HIGH){
      //Serial.println("Error: Tray out of position.");
      Serial.println("0");
      stepper.stop();
      isHomed = false;
      return;
    }
  }

  //Move the carriage back to the left end. Sensor is still collecting data.
  stepper.moveTo(0);
  while ((stepper.distanceToGo() != 0) && (millis() - startTime < 10000)) {
    stepper.run();
    // Check if either limit switch is pressed after each step
    if (digitalRead(LEFT_LIMIT_SWITCH_PIN) == LOW || digitalRead(RIGHT_LIMIT_SWITCH_PIN) == LOW) {
      stepper.stop();
      //Serial.println("Scan unsuccessful: Limit switch triggered.");
      Serial.println("0");
      isHomed = false;
      return;
    }
  }

  //Serial.println("Scan successful.");
  Serial.println("1");
}