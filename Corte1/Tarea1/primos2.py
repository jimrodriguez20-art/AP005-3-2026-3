# Inicializa la variable de control 'a' con el entero 1; sirve como bandera/condición para mantener activo el bucle principal.
a = 1
# Solicita un valor al usuario por consola y lo almacena como texto (str) en 'value'; obtiene el límite superior inicial para evaluar primos.
value = input('Ingrese un valor')
# Convierte la cadena 'value' a un número entero (int) y la reasigna a 'value'; define el rango numérico a procesar.
value = int(value)

# Inicia un bucle 'while' que se repetirá mientras 'a' sea igual a 1; permite repetir el proceso si el usuario lo desea.
while a == 1:
    # Genera una secuencia de enteros 'i' desde 1 hasta el valor de 'value' inclusive; itera sobre cada número a evaluar.
    for i in range(1, value + 1):
        # Reinicia la variable 'conta' a 0 para el entero 'i' actual; prepara el contador de divisores exactos.
        conta = 0
        # Inicia un bucle interno para iterar 'n' desde 1 hasta 'i' inclusive; prueba todos los posibles divisores de 'i'.
        for n in range(1, i + 1):
            # Calcula el residuo de dividir 'i' entre 'n' usando el operador módulo (%); verifica si la división es exacta.
            residue = i % n
            # Evalúa si el residuo es cero; detecta cuando 'n' es un divisor exacto de 'i'.
            if residue == 0:
                # Incrementa el contador 'conta' en 1; registra la presencia de un divisor encontrado.
                conta = conta + 1
            
            # Impresión comentada de depuración; mostraba el valor del número evaluado en la iteración.
            # print("i = ", i)
            # Impresión comentada de depuración; mostraba el divisor actual que se estaba probando.
            # print("n = ", n)
            # Impresión comentada de depuración; mostraba el residuo resultante de la operación módulo.
            # print("residue = ", residue)
            # Impresión comentada de depuración; mostraba el acumulado actual de divisores encontrados.
            # print("conta = ", conta)
    # *Nota de lógica*: Al estar fuera del bucle 'for i', esta condición solo evalúa el estado final del ÚLTIMO valor de 'i'.
    if conta == 2:
        # Se ejecuta si el último valor evaluado tiene exactamente 2 divisores; indica que ese último número es primo.
        print(f'{i} es un primo')
        # Imprime un salto de línea adicional para dar espacio en la salida de consola.
        print("\n")
    # Define la ruta alternativa cuando 'conta' es diferente de 2 en el último valor evaluado.
    else:
        # Imprime que el último valor evaluado no es un número primo.
        print(f'{i} NOOO es un primo')
        # Imprime un salto de línea adicional para separar la salida gráfica.
        print("\n")

    # Muestra en pantalla el mensaje preguntando al usuario si desea continuar en el programa.
    print('Do you want to continue?. Press 1 to do that')
    # Captura la respuesta ingresada por el usuario como una cadena de texto y la guarda en 'a'.
    a = input()
    # Convierte la respuesta almacenada en 'a' a un número entero; actualiza el valor de la bandera de control.
    a = int(a)

    # Comprueba si el valor ingresado en 'a' es diferente de 1; determina si el usuario desea salir del programa.
    if a != 1:
        # Interrumpe y finaliza inmediatamente la ejecución del bucle 'while'; fuerza la salida del ciclo.
        break

    # Pide un nuevo valor numérico si el usuario decidió continuar; actualiza el límite para la siguiente iteración del 'while'.
    value = input('Ingrese un valor')
    # Convierte el nuevo dato a número entero y lo asigna a 'value'; prepara la siguiente evaluación.
    value = int(value)
