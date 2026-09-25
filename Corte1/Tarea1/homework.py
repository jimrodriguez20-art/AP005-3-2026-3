# Solicita al usuario ingresar un valor por consola y lo almacena como cadena de texto (str) en 'a'; obtiene el primer dato de entrada.
a = input("Enter a number: ")
# Convierte el valor de 'a' de texto a un número entero (int) y reasigna el resultado a 'a'; define el tipo numérico del primer valor.
a = int(a)
# Solicita al usuario ingresar un segundo valor por consola y lo almacena como texto (str) en 'b'; obtiene el segundo dato de entrada.
b = input("Enter b number: ")
# Convierte el valor de 'b' a un número de punto flotante (float) y lo reasigna a 'b'; define el segundo valor como decimal.
b = float(b)
# Suma el entero 'a' y el flotante 'b', promocionando implícitamente el resultado a flotante en 'c'; realiza la operación aritmética principal.
c = a + b

# Compara si el valor numérico de 'a' es equivalente al valor de 'b' (independientemente del tipo de dato); evalúa la igualdad de magnitud.
if a == b:
    # Se ejecuta si 'a' y 'b' representan el mismo valor numérico (p. ej. 5 y 5.0); notifica la equivalencia de valores.
    print("equal")
# Define la ruta de ejecución alternativa en caso de que la comparación 'a == b' resulte falsa; gestiona valores numéricos distintos.
else:
    # Se ejecuta cuando los valores numéricos de 'a' y 'b' no son iguales; notifica que las magnitudes difieren.
    print("Different")

# Imprime en consola el tipo de dato actual de 'a' usando type(); confirma visualmente que 'a' es de tipo 'int'.
print("Type of a is: ", type(a))
# Imprime en consola el tipo de dato actual de 'b' usando type(); confirma visualmente que 'b' es de tipo 'float'.
print("Type of b is: ", type(b))
# Imprime el valor resultante de la suma guardada en 'c'; muestra el resultado numérico final de la operación.
print("c = ", c)

# Compara directamente los tipos de dato devueltos por type(a) y type(b) (int vs float); evalúa la igualdad estricta de clases de objetos.
if type(a) == type(b):
    # Se ejecutaría solo si ambas variables compartieran el mismo tipo de dato; en este script nunca se cumple pues int != float.
    print("a and b are of the same type")
# Define la rama alternativa cuando la comparación de tipos de datos resulta falsa; maneja el caso de tipos disímiles.
else:
    # Se ejecuta porque 'int' y 'float' son tipos distintos en Python; notifica la disparidad de clases entre variables.
    print("a and b are of different type")
