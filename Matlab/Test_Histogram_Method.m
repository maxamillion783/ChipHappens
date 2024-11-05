% Test of method using histogram gaussian distributions to differentiate
% double and triple peaks
% by Zoe Cremona

close all; clear all; hold off;

% Constants
SAMPLE_RATE = 0.001; % Sensor takes data every SAMPLE_RATE seconds

% Read and format the data
rawData = readtable('../TestData/AP-DATA-004_10-22_trial_1_400mm_1000us_black_solid.csv', 'NumHeaderLines',12);
y = table2array(rawData(:,"Var2"))';

% Low-pass filter
cutoff_frequency = 0.0001; % Adjust cutoff frequency to suit your needs
y_filt = lowpass(y, cutoff_frequency);

% Counting Mechanism
x_peaks = [];
y_peaks = [];                    % Empty array of all found peaks
count = 0;                       % Initialize count for positive to negative transitions
num_entries = length(y);         % Total number of entries in y

% Loop to calculate the derivative between every 2 entries in y
der_y = firstDeriv(y_filt, SAMPLE_RATE);

% Count transitions from positive to negative in der_y
for i = 2:length(der_y)     % Start from the second entry to compare with the previous one
     % Change from positive to non-positive
     % Filter out wildly out of range points
     if der_y(i) <= 0 && der_y(i-1) > 0 && y_filt(i) > 1 && y_filt(i) <3 
         count = count + 1;   % Increment count for negative transition
         y_peaks(end+1) = y_filt(i-1); % Track all found peaks
         x_peaks(end+1) = (i-1)*SAMPLE_RATE;
         
     end
end

% Plot results
x = 0:SAMPLE_RATE:(length(y_filt)-1)*SAMPLE_RATE;

figure(1)
plot(x, y_filt)
hold on;
plot(x_peaks, y_peaks, 'o', 'MarkerSize', 8, 'MarkerFaceColor', 'b');

figure(2)
hold off;
histogram(y_peaks, 25)

% Compute the first derivative using a centered difference method for
% middle points and one-sided difference for ends
% Consider using one-sided difference for all points
function df = firstDeriv(y,h)
    % Use O(h^2) approximations to compute derivative
    % y = evenly spaced data of outputs
    % h = spacing between the inputs of the data points (delta x)
    % df = derivative of y with respect to x
    n = length(y);
    df = zeros(1, n);
    
    df(1) = (-3*y(1)+4*y(2)-y(3))/(2*h);
    df(n) = (3*y(n)-4*y(n-1)+y(n-2))/(2*h);
    
    for i=2:n-1
        df(i) = (y(i+1)-y(i-1))/(2*h);
    end
end