T = readtable('data.csv', 'Delimiter', '\t');  % Lee el archivo con separador tabulación %[output:51920340]
% Asignación correcta de columnas
col1 = T.t;    % tiempo
col2 = T.x;    % x
col3 = T.y;    % y
col4 = T.z;    % z
col4 = T.magnitud;    % mag
% Gráfica 1: x vs t
figure;
plot(col1, col2);
xlabel('Tiempo (s)');
ylabel('Aceleración lineal en x');
title('Gráfica de aceleración lineal en x vs tiempo');
grid on;
% Gráfica 2: y vs t
figure;
plot(col1, col3);
xlabel('Tiempo (s)');
ylabel('Aceleración lineal en y');
title('Gráfica de aceleración lineal en y vs tiempo');
grid on;
% Gráfica 3: z vs t
figure;
plot(col1, col4);
xlabel('Tiempo (s)');
ylabel('Aceleración lineal en z');
title('Gráfica de aceleración lineal en z vs tiempo');
grid on;

% Gráfica 4: aceleración absoluta vs t
figure;
plot(col1, col4);
xlabel('Tiempo (s)');
ylabel('Aceleración absoluta');
title('Gráfica de aceleración absoluta vs tiempo');
grid on;


%[appendix]{"version":"1.0"}
%---
%[metadata:view]
%   data: {"layout":"onright","rightPanelPercent":15.9}
%---
%[output:51920340]
%   data: {"dataType":"error","outputData":{"errorType":"runtime","text":"Error using <a href=\"matlab:matlab.lang.internal.introspective.errorDocCallback('readtable', 'C:\\Program Files\\MATLAB\\R2025a\\toolbox\\matlab\\io\\tabular\\iofun\\readtable.m', 19)\" style=\"font-weight:bold\">readtable<\/a> (<a href=\"matlab: opentoline('C:\\Program Files\\MATLAB\\R2025a\\toolbox\\matlab\\io\\tabular\\iofun\\readtable.m',19,0)\">line 19<\/a>)\nUnable to find or open 'data.csv'. Check the path and filename or file permissions."}}
%---
