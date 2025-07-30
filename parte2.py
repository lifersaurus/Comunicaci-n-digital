import csv
import matplotlib.pyplot as plt

t_values = []
l_values = []

with open('luz.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='\t')
    for row in csv_reader:
        t_values.append(float(row['t']))
        l_values.append(float(row['Luminance']))
       

# Graficar
plt.plot(t_values, l_values, label='x', color='orange')
plt.xlabel('Tiempo (s)')
plt.ylabel('luminancia')
plt.title('luminancia en x vs. Tiempo')
plt.grid(True)
plt.tight_layout()
plt.show()

