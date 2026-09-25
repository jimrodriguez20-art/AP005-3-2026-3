# Importa el módulo 'time' de la biblioteca estándar de Python; proporciona herramientas para medir el tiempo de ejecución del script.
import time
# Registra el tiempo de inicio de la ejecución en segundos (época Unix) usando time.time(); sirve como marca temporal base para el rendimiento.
inicio = time.time()

# Inicia un bucle 'for' para iterar 'i' de 1 a 30 (el 31 es excluyente); define el rango numérico positivo a evaluar para hallar números primos.
for i in range(1, 31):
    # Inicializa el contador 'conta' en 0 en cada iteración del bucle exterior; reinicia la cuenta de divisores exactos para el número 'i' actual.
    conta = 0
    # Inicia un bucle interno para iterar 'n' desde 1 hasta el valor de 'i' inclusive ('i+1'); prueba cada posible divisor dentro del rango.
    for n in range(1, i + 1):
        # Calcula el residuo de la división entera entre 'i' y 'n' mediante el operador módulo (%); sirve para verificar la divisibilidad.
        residue = i % n
        # Comprueba si el residuo es exactamente cero; determina si 'n' divide a 'i' de manera exacta sin dejar resto.
        if residue == 0:
            # Incrementa en 1 la variable 'conta'; acumula la cantidad total de divisores encontrados para el número 'i' evaluado.
            conta = conta + 1
            
    # Evalúa si el número total de divisores es igual a 2; aplica la definición estricta de número primo (divisible solo entre 1 y sí mismo).
    if conta == 2:
        # Imprime en consola que el entero 'i' es un número primo mediante una f-string; notifica los aciertos de la prueba de primalidad.
        print(f'{i} es un primo')
        # Imprime un salto de línea adicional en la consola; genera una separación visual limpia entre las salidas reportadas.
        print("\n")

# Registra la marca de tiempo inmediatamente después de finalizar los bucles; captura el momento final de la ejecución.
fin = time.time()
# Resta 'inicio' a 'fin' para obtener el tiempo transcurrido en segundos, lo multiplica por 1000 para llevarlo a milisegundos y lo imprime.
print("t = ", (fin - inicio) * 1000)
