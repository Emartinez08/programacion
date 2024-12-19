import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la función
def func(x1, x2):
    return 17.73 + 0.025*x1 + 0.400*x2 - 1.84*x1**2 - 1.89*x2**2 + 0.25*x1*x2
    #return 80 + 4*x1 + 8*x2 - 4*x1*2 - 12*x2*2 - 12*x1*x2

# Crear un rango de valores para x1 y x2
x1 = np.linspace(-10, 10, 100)  # Rango de valores para x1
x2 = np.linspace(-10, 10, 100)  # Rango de valores para x2

# Crear una malla de coordenadas (x1, x2)
x1, x2 = np.meshgrid(x1, x2)

# Calcular los valores de la función en la malla
z = func(x1, x2)

# Crear el gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
ax.plot_surface(x1, x2, z, cmap='viridis')

# Etiquetas del gráfico
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f(x1, x2)')
ax.set_title('Gráfico de la función')

# Mostrar el gráfico
plt.show()
