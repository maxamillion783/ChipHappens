% Parameters
num_cards = 500; % Number of cards we are counting in this data
samples_per_card = 100;% Number of measurements we will take over one card
theta = 45;% Angle of the cards [deg]
t_card = 0.033;% Thickness of the card [in]

% Wave properties derived from parameters
period = t_card*sind(theta)*tand(theta)+t_card*cosd(theta);% Period [in]
x = linspace(0, num_cards*period, samples_per_card*num_cards);% x-length of waveform we export [in]
y = zeros(size(x));% storing all of our y points
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
end

% Plot the triangle wave
plot(x, y);
xlabel('x');
ylabel('y');
title('Triangle Waveform (Uneven Legs)');
axis equal;
grid on;