# Inicia un bucle que iterará la variable 'i' desde 1 hasta 20 (el límite 21 es excluyente); define el rango de números a analizar.
# for i in range (1,21):
# Calcula el residuo de dividir 'i' entre 2 mediante el operador módulo (%) y lo asigna a 'residual'; determina si el número es par o impar.
#     residual = i%2
# Evalúa si 'residual' es igual a cero; actúa como el condicional que identifica a los números pares.
#     if residual == 0:
# Imprime en consola que el valor de 'i' es par usando una f-string formateada; muestra el resultado de la rama verdadera del condicional.
#         print(f'{i} is even')
# Define la ruta alternativa del condicional 'if'; se ejecuta únicamente cuando el residuo es diferente de cero (números impares).
#     else:
# Línea comentada que utilizaba f-strings para imprimir que 'i' es impar; sirve como alternativa de formateo de texto.
#         #print(f'{i} is odd')
# Imprime en consola que 'i' es impar convirtiendo 'i' a texto mediante str() y concatenando cadenas (+); muestra el resultado para impares.
#         print(str(i) + ' is odd')

# Inicia un bucle que iterará la variable 'i' desde 0 hasta 5 (el límite 6 es excluyente); define la secuencia base para el cálculo de potencias.
# for i in range (0,6):
# Eleva el valor actual de 'i' al cubo usando el operador de potencia (**) y asigna el resultado a 'result'; calcula $i^3$.
#     result = i**3
# Imprime en consola el valor almacenado en 'result'; muestra la potencia cúbica obtenida en cada iteración.
#     print(result)

# Solicita al usuario ingresar un número por consola y lo guarda como cadena de texto (str) en 'times'; obtiene el dato de entrada inicial.
times = input("Enter a number of times: ")
# Convierte la cadena 'times' a número flotante (float) y la reasigna a 'times'; permite procesar temporalmente entradas con notación decimal.
times = float(times)
# Trunca el valor flotante de 'times' eliminando la parte decimal para dejarlo como entero (int); asegura un tipo discreto para el rango.
times = int(times)
# Imprime en consola el tipo de dato final de 'times' mediante type(); confirma visualmente que la variable se transformó a 'int'.
print(type(times))
# Imprime el valor entero final almacenado en 'times'; muestra al usuario el límite procesado que controlará el bucle.
print(times)

# Compara si el entero 'times' es exactamente igual a cero; evalúa el caso límite donde no se deben ejecutar iteraciones.
if times == 0:
    # Imprime en consola "Don't do anything"; notifica la inactividad del programa cuando el usuario ingresa cero.
    print("Don't do anything")
# Define la rama de ejecución alternativa en caso de que 'times' sea distinto de cero; gestiona los casos ejecutables.
else:
    # Genera un bucle que va desde 1 hasta el valor de 'times' inclusive (gracias a 'times + 1'); controla la cantidad de repeticiones del código.
    for i in range(1, times + 1):
        # Imprime en consola el texto "i = " seguido del contador 'i' en cada vuelta; muestra el avance ordinal de la iteración actual.
        print("i = ", i)
