import numpy as np
import matplotlib.pyplot as plt

# =====================================
# GRAFICA 1: ERRORES POR EPOCA
# =====================================

errores = np.loadtxt("errores.dat", ndmin=2)

epocas = errores[:, 0]
cantidad_errores = errores[:, 1]

plt.figure(figsize=(10, 6))

plt.plot(
    epocas,
    cantidad_errores,
    marker='o',
    linewidth=2,
    label='Errores por epoca'
)

plt.title("Aprendizaje del perceptron")
plt.xlabel("Numero de epoca")
plt.ylabel("Cantidad de errores")

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("errores_matplotlib.png")
plt.show()


# =====================================
# GRAFICA 2: VARIABLE Z
# =====================================

datos_z = np.loadtxt("z_por_epoca.dat", ndmin=2)

epocas_z = datos_z[:, 0]

plt.figure(figsize=(10, 6))

for i in range(1, 5):

    plt.plot(
        epocas_z,
        datos_z[:, i],
        marker='o',
        linewidth=2,
        label=f'Patron {i}'
    )

plt.axhline(y=0, linestyle='--', label='Umbral z = 0')

plt.title("Evolucion de la variable z")
plt.xlabel("Numero de epoca")
plt.ylabel("Valor de z")

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("valores_z_matplotlib.png")
plt.show()
