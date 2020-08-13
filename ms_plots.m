%% alpha accuracy plot (with 0)
clear; clc; close all;

fname = 'exported_data/best_acc_&_alphas.csv';
svc = readtable(fname);
mz = 2000:1:20000;

plot(mz, svc.accuracy, 'DisplayName','Accuracy curve')
title('Accuracy of separating S & R with \alpha at a given mol. weight m/z','FontSize',22)
xlabel('Molecular Weight (m/z)','FontSize',22)
ylabel('Accuracy (%)','FontSize',22)
yline(mean(svc.accuracy), 'DisplayName','Mean acc. = 99.63%')
legend('FontSize', 20);
xlim([2000 7000]);
set(gcf, 'Position',  [500, 300, 1500, 500])

%% alpha accuracy plot (with confidence screening)
clear; clc; close all;
% 
% fname = 'exported_data/best_acc_&_alphas.csv';
fname = 'exported_data/best_acc_&_alphas_no_0.csv';
svc = readtable(fname);

% set min confidence level for displayed data points
ct = 1;
conf = 5;
for i=1:height(svc)
    if svc.confidence(i) > conf
        new_svc(ct,:) = svc(i,:);
        mz(ct) = 1999 + i;
        ct = ct + 1;
    end
end

% get confidence arrays of different levels
ct_20 = 1; ct_10 = 1; ct_0 = 1;
for i=1:height(new_svc)
    if new_svc.confidence(i) > 20
%         plot(mz(i), new_svc.accuracy(i), 'g*') %, 'DisplayName','>20% data pts have this peak'
        svc_20(ct_20,:) = [mz(i); new_svc.accuracy(i)];
        ct_20 = ct_20 + 1;
    elseif new_svc.confidence(i) > 10
%         plot(mz(i), new_svc.accuracy(i), 'bo')
        svc_10(ct_10,:) = [mz(i); new_svc.accuracy(i)];
        ct_10 = ct_10 + 1;
    else
%         plot(mz(i), new_svc.accuracy(i), 'rx')
        svc_0(ct_0,:) = [mz(i); new_svc.accuracy(i)];
        ct_0 = ct_0 + 1;
    end
    hold on;
end

% plot
plot(mz, new_svc.accuracy, 'DisplayName','Accuracy curve')
hold on; grid on;
plot(svc_20(:,1), svc_20(:,2), '*', 'Color',[0.4660, 0.6740, 0.1880], 'DisplayName','>20% entries have this peak')
plot(svc_10(:,1), svc_10(:,2), 'bo', 'DisplayName','10~20% entries have this peak')
plot(svc_0(:,1), svc_0(:,2), 'rx', 'DisplayName','<10% entries have this peak')
title('Accuracy of separating S & R with \alpha at a given mol. weight m/z','FontSize',22)
xlabel('Molecular Weight (m/z)','FontSize',22)
ylabel('Accuracy (%)','FontSize',22)
yline(mean(new_svc.accuracy), 'DisplayName','Mean acc. = 59.98%')
% yline(90)
legend('FontSize', 16);
xlim([2000 3000]);
set(gcf, 'Position',  [500, 300, 1500, 500])

%% accuracy histogram
q = quantile(new_svc.accuracy, [0.25 0.5 0.75 0.95]);
max = max(new_svc.accuracy);
min = min(new_svc.accuracy);
% avg = mean(new_svc.accuracy);
lgd_txt = sprintf('Min acc. = %.1f\nQ1 = %.1f\nQ2 = %.1f\nQ3 = %.1f\nMax acc. = %.1f', min, q(1), q(2), q(3), max);
histogram(new_svc.accuracy, 'DisplayName',lgd_txt)
title('Accuracy histogram of X (m/z) = 2000~20000','FontSize',22)
xlabel('Accuracy (%)', 'FontSize',22)
ylabel('Count', 'FontSize',22)
legend('FontSize',18)
set(gcf, 'Position',  [500, 300, 1000, 500])

%% alpha plot
plot(mz, new_svc.alpha)
title('\alpha for X (m/z) = 2000~7000','FontSize',22)
xlabel('Molecular Weight (m/z)','FontSize',22)
ylabel('\alpha value', 'FontSize',22)
xlim([2000 7000]);
set(gcf, 'Position',  [500, 300, 1500, 500])

%% alpha zoom in X = 2415
clear; clc; close all;

fname = 'exported_data/foo.csv';
inten = table2array(readtable(fname));

xline(27500, 'DisplayName','\alpha = 21508', 'FontSize',22)
hold on; legend;
legend off;

for i=1:length(inten)
    if inten(i,2) == 1
        plot(inten(i,1), 2415, 'bo')
        hold on;
    else
        plot(inten(i,1), 2415, 'ro')
        hold on;
    end
end
xlabel('Intensity level of X = 2415','FontSize',22)
ylabel('X', 'FontSize',22)
set(gcf, 'Position',  [500, 300, 1500, 500])
% plot(inten(:,1), ones(243,1)')