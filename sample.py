from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn

seaborn.set()

# se crea un array de 10 filas y dos columnas
X = random.rand(10, 2)
# se imprime el array aleatorio
print(X)
# se imprimen las componentes x
print(X[:, 0])
# se imprimen las componentes y
print(X[:, 1])
# se hace un scatter de esos puntos, el parametro s es para el tamaño de las bolitas.
plt.scatter(X[:, 0], X[:, 1], s=100)
plt.show()

# se calcula la distancia euclidea entre los puntos
dist_sq = np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2, axis=-1)
print("distancia")
print(dist_sq)

# for each pair of points, compute differences in their coordinates
differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]

print(differences.shape)

