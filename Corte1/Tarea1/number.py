# Importa el módulo 'random' de la biblioteca estándar de Python; proporciona funciones para la generación de números pseudoaleatorios.
import random
# Importa el submódulo 'pyplot' de Matplotlib bajo el alias 'plt'; ofrece la interfaz gráfica para crear y personalizar visualizaciones.
from matplotlib import pyplot as plt

# Comentario indicativo original del script para ubicar el desarrollo del código.
# Add your code below:
# Crea un objeto 'range' con enteros de 1 a 12 (el 13 es excluyente); define los valores del eje horizontal (eje X) del gráfico.
numbers_a = range(1, 13)
# Genera una lista de 12 números enteros aleatorios entre 1 y 1000 mediante comprensión de listas; establece las coordenadas del eje vertical (eje Y).
numbers_b = [random.randint(1, 1000) for i in range(12)]
# Relaciona los pares ordenados (X, Y) de 'numbers_a' y 'numbers_b' para trazar una gráfica de líneas; construye la figura en memoria.
plt.plot(numbers_a, numbers_b)
# Renderiza y muestra en pantalla la ventana del gráfico generado; concluye el proceso de visualización del lienzo.
plt.show()
