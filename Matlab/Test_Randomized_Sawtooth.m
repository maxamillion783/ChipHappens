% Parameters
num_cards = 523; % Number of cards we are counting in this data
samples_per_card = 100;% Number of measurements we will take over one card
theta = 46;% Angle of the cards [deg]
%t_card was .033
t_card = 0.0299;% Thickness of the card [in]

% Wave properties derived from parameters
period = t_card*sind(theta)*tand(theta)+t_card*cosd(theta);% Period [in]
x = linspace(0, num_cards*period, samples_per_card*num_cards);% x-length of waveform we export [in]
y = zeros(size(x));% storing all of our y points
der_y = zeros(size(x));%points for derivative list
y_filt = zeros(size(x)); %filtered sawtooth wave
duty_cycle = (t_card*sind(theta)*tand(theta))/period;% Percent of the period that is rising
x_mod = mod(x, period);% x values within a single period
amplitude = t_card*sind(theta);% Amplitude of the peaks [in]

% Calculate
for i = 1:length(x_mod)
    if x_mod(i) < duty_cycle * period
        % Rising edge: y = (slope_up) * x
        y(i) = (amplitude / (duty_cycle * period)) * x_mod(i);
    else
        % Falling edge: y = amplitude - (slope_down) * x
        y(i) = amplitude - (amplitude / ((1 - duty_cycle) * period)) * (x_mod(i) - duty_cycle * period);
    end
    y(i) = y(i) + rand(1,1)/150;
end

% Low-pass filter
cutoff_frequency = 0.0001; % Adjust cutoff frequency to suit your needs
y_filt = lowpass(y, cutoff_frequency);

% Counting Mechanism
count = 0;               % Initialize count for positive to negative transitions
num_entries = length(y); % Total number of entries in y
der_y = [];              % Initialize der_y as an empty array

% Loop to calculate the derivative (difference) between every 2 entries in y
for i = 30:num_entries-30  % Iterate up to the second last entry
    derivative = y_filt(i+30) - y_filt(i);  % Calculate the derivative
    der_y(end + 1) = derivative;  % Append the derivative to der_y
end

% Count transitions from positive to negative in der_y
for i = 2:length(der_y)     % Start from the second entry to compare with the previous one
     if der_y(i) <= 0 && der_y(i-1) > 0 % Change from positive to non-positive
         count = count + 1;   % Increment count for negative transition
     end
end

% Display the result
disp(['Total Card Count: ', num2str(count)]);

% Plot the triangle wave
subplot(2, 1, 1);
plot(x, y);
xlabel('x');
ylabel('y');
title('Original Triangle Waveform (Uneven Legs)');
axis equal;
grid on;

% Plot the filtered wave
subplot(2, 1, 2);
plot(x, y_filt);
xlabel('x');
ylabel('y');
title('Filtered Triangle Waveform (Smoothed)');
axis equal;
grid on;
