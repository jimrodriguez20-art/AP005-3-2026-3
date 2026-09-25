# Importa el módulo 'time' de la biblioteca estándar de Python; proporciona herramientas para medir el tiempo de ejecución del script.
import time
# Registra el tiempo de inicio de la ejecución en segundos (época Unix) usando time.time(); sirve como marca temporal base para la medición.
inicio = time.time()

# Inicia un bucle 'for' para iterar el entero 'i' de 0 a 30 (el 31 es excluyente); establece el rango de candidatos a evaluar como números primos.
for i in range(0, 31):
    # Inicializa en cero el contador 'conta' en cada vuelta del bucle exterior; restablece el acumulador de divisores exactos para el valor actual de 'i'.
    conta = 0
    # Inicia un bucle interno para iterar 'n' desde 1 hasta el valor actual de 'i' inclusive ('i+1'); prueba todos los posibles divisores.
    for n in range(1, i + 1):
        # Calcula el residuo de dividir 'i' entre 'n' mediante el operador módulo (%); evalúa la divisibilidad de 'i'.
        residue = i % n
        # Comprueba si el residuo es cero; verifica si 'n' es un divisor exacto (sin residuo) de 'i'.
        if residue == 0:
            # Incrementa el contador 'conta' en 1 cuando la división es exacta; registra la presencia de un divisor encontrado.
            conta = conta + 1
            
    # Evalúa si 'conta' es igual a 2; aplica la definición de número primo (aquel que tiene exactamente dos divisores positivos: 1 y él mismo).
    if conta == 2:
        # Imprime en consola que el entero 'i' es primo mediante una f-string; muestra únicamente los valores que satisfacen la condición de primalidad.
        print(f'{i} es un primo')
        
# Registra el tiempo actual de finalización en segundos usando time.time(); captura la marca temporal posterior a la ejecución del algoritmo.
fin = time.time()
# Calcula el tiempo transcurrido (fin - inicio), lo convierte a milisegundos multiplicando por 1000 y lo imprime; mide el rendimiento del proceso.
print("t = ", (fin - inicio) * 1000)
