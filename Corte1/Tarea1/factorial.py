# Inicia un bucle infinito que mantendrá el programa ejecutándose continuamente hasta que sea interrumpido externamente; permite solicitar datos repetidamente.
while True:
    # Captura la entrada del usuario como texto mediante input(), la convierte a entero con int() y la asigna a 'value'; obtiene el dato base para el cálculo.
    value = int(input("Enter a positive integer value: "))
    # Imprime en consola el texto "Value: " seguido del número ingresado; sirve para confirmar visualmente al usuario el valor capturado.
    print("Value: ", value)
    # Evalúa si la variable 'value' es de tipo entero (int) y guarda el resultado booleano (True/False) en 'a'; prepara una verificación de tipo de dato.
    a = isinstance(value, int)
    # Comprueba si 'a' es True y si 'value' es mayor a cero; actúa como la estructura de control que decide si se calcula el factorial o se muestra un error.
    if a == True and value > 0:
        # Declara la variable 'fact' y la inicializa en 1; sirve como el elemento neutro multiplicativo para acumular el resultado del factorial.
        fact = 1
        # Genera una secuencia de enteros desde 1 hasta 'value' (incluido); controla el número de iteraciones necesarias para el cálculo del factorial.
        for i in range(1, value + 1):
            # Multiplica el valor actual acumulado en 'fact' por el entero 'i' de la iteración actual; realiza el cálculo iterativo del factorial ($n!$).
            fact = fact * i
        # Imprime el resultado final del factorial utilizando una f-string formateada; muestra al usuario el cálculo completado con su valor original.
        print(f'The factorial of {value} is: ', fact)
    # Define la rama alternativa del condicional 'if'; se ejecuta únicamente si la entrada ingresada no cumple con ser mayor a cero.
    else:
        # Muestra un mensaje de advertencia indicando que el número debe ser un entero positivo; retroalimenta al usuario cuando la validación falla.
        print("Please, enter a positive integer number")
