close all; clear all;

M = readtable('C:/ChipHappens/TestData/AP-DATA-008_10-22_trial_5_400mm_1000us_1000Hz_ambient-filter_white-clear.csv', 'NumHeaderLines',12);

t = table2array(M(:,"Var2"))';
tt = zeros(1,length(t));
N = 13;
Nby2Floor = floor(N/2);
Nby2Ciel = floor(N/2)+1;

for i = 1:length(t)-Nby2Floor
    if (i < Nby2Ciel)
        tt(i) = t(i);
    else
        for j= -Nby2Floor:Nby2Floor
            tt(i) = tt(i)+(1/N)*t(i+j);
        end
    end
end

figure(1);
subplot(2,1,1);
plot(t);
subplot(2,1,2);
plot(tt);