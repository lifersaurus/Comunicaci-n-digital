import csv
import matplotlib.pyplot as plt # type: ignore

t_values = []
x_values = []
y_values = []
z_values = []
a_values = []
with open('data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='\t')
    for row in csv_reader:
        t_values.append(float(row['t']))
        x_values.append(float(row['x']))
        y_values.append(float(row['y']))
        z_values.append(float(row['z']))
        a_values.append(float(row['magnitud']))

# Graficar
plt.plot(t_values, x_values, label='x', color='green')
plt.xlabel('Tiempo (s)')
plt.ylabel('Aceleración lineal en x')
plt.title('Aceleración lineal en x vs. Tiempo')
plt.grid(True)
plt.tight_layout()
plt.show()
# Graficar
plt.plot(t_values, y_values, label='y', color='blue')
plt.xlabel('Tiempo (s)')
plt.ylabel('Aceleración lineal en y')
plt.title('Aceleración lineal en y vs. Tiempo')
plt.grid(True)
plt.tight_layout()
plt.show()

# Graficar
plt.plot(t_values, z_values, label='z', color='yellow')
plt.xlabel('Tiempo (s)')
plt.ylabel('Aceleración lineal en z')
plt.title('Aceleración lineal en z vs. Tiempo')
plt.grid(True)
plt.tight_layout()
plt.show()
# Graficar
plt.plot(t_values, a_values, label='a', color='black')
plt.xlabel('Tiempo (s)')
plt.ylabel('Aceleración absoluta')
plt.title('Aceleración absoluta vs. Tiempo')
plt.grid(True)
plt.tight_layout()
plt.show()
