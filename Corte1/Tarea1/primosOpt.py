# 9) Imprimir los números primos existentes entre 0 y 30
# Define el límite superior estricto del rango numérico a evaluar (hasta 29 inclusive); sirve como cota para el bucle.
tope_rango = 30
# Inicializa la variable 'n' en 0; actuará como el contador del número entero actual evaluado.
n = 0
# Inicializa la bandera booleana 'primo' en True; asume por defecto que el número 'n' es primo hasta demostrar lo contrario.
primo = True
# Inicia un bucle 'while' que se ejecuta mientras 'n' sea menor a 'tope_rango' (30); controla la iteración del rango.
while (n < tope_rango):
    # Recorre posibles divisores 'div' desde 2 hasta n-1; si n < 2, este rango queda vacío y el bucle for no se ejecuta.
    for div in range(2, n):
        # Evalúa mediante el operador módulo (%) si 'n' es divisible exactamente entre 'div' (residuo igual a cero).
        if (n % div == 0):
            # Cambia la bandera 'primo' a False al encontrar al menos un divisor exacto; identifica que 'n' es compuesto.
            primo = False
    # Evalúa si la variable booleana 'primo' se mantuvo como True al finalizar la revisión de divisores.
    if (primo):
        # Imprime en consola el valor de 'n' reconocido como número primo; despliega el resultado hallado.
        print(n)
    # Define la ruta alternativa cuando 'primo' es False (el número no era primo).
    else:
        # Restablece la bandera 'primo' a True para prepararla para la evaluación del siguiente número.
        primo = True
    # Incrementa el contador 'n' en 1; avanza al siguiente entero dentro de la secuencia.
    n += 1


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
# Reorganiza el contador 'n' reiniciándolo en 0; prepara el entorno para la segunda versión del algoritmo.
n = 0
# Inicializa la bandera 'primo' en True para comenzar el ciclo de comprobación de la versión optimizada.
primo = True
# Inicia el bucle 'while' principal controlando la cota máxima del rango de números a evaluar.
while (n < tope_rango):
    # Recorre posibles divisores 'div' desde 2 hasta n-1 para comprobar la divisibilidad del número 'n'.
    for div in range(2, n):
        # Comprueba si existe división exacta entre el candidato 'n' y el divisor 'div'.
        if (n % div == 0):
            # Marca la variable booleana 'primo' como False al encontrar un divisor válido.
            primo = False
            # Interrumpe y sale inmediatamente del bucle 'for' sin probar los demás divisores; aplica la optimización clave.
            break
    # Comprueba si la bandera 'primo' permanece activa como True tras la interrupción o finalización del bucle 'for'.
    if (primo):
        # Imprime el número primo identificado en pantalla.
        print(n)
    # Ruta ejecutada si la bandera resultó falsa (número compuesto).
    else:
        # Restablece la bandera booleana 'primo' a True para el siguiente número del ciclo.
        primo = True
    # Incrementa el contador 'n' para pasar al siguiente candidato a primo.
    n += 1

# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
# Declara e inicializa un contador acumulativo para registrar las iteraciones totales realizadas sin la instrucción 'break'.
ciclos_sin_break = 0
# Reinicia el contador de números 'n' en 0 para iniciar la medición de ciclos.
n = 0
# Inicializa la bandera booleana de apoyo 'primo' en True.
primo = True
# Bucle 'while' que controla la iteración sobre cada número candidato dentro del rango tope (30).
while (n < tope_rango):
    # Bucle 'for' que itera sobre los divisores 'div' comprobando la divisibilidad.
    for div in range(2, n):
        # Incrementa en 1 la variable métrica 'ciclos_sin_break' por cada iteración efectuada dentro del bucle interno.
        ciclos_sin_break += 1
        # Verifica si 'div' es un divisor exacto de 'n'.
        if (n % div == 0):
            # Cambia la bandera 'primo' a False sin detener la prueba con otros divisores.
            primo = False
    # Evalúa si se confirmó que 'n' es primo.
    if (primo):
        # Imprime el número primo en la consola.
        print(n)
    # Maneja la alternancia cuando 'n' no es primo.
    else:
        # Restablece el indicador 'primo' a True para la siguiente iteración del 'while'.
        primo = True
    # Avanza al siguiente entero del rango.
    n += 1
# Imprime la suma total de iteraciones registradas en la versión no optimizada concatenando cadenas.
print('Cantidad de ciclos: ' + str(ciclos_sin_break))


# Declara e inicializa el contador de iteraciones para la versión optimizada con 'break'.
ciclos_con_break = 0
# Reinicia el número inicial a evaluar en 0.
n = 0
# Inicializa la bandera 'primo' en True.
primo = True
# Bucle 'while' principal de la ejecución de pruebas con 'break'.
while (n < tope_rango):
    # Recorre divisores desde 2 hasta n-1.
    for div in range(2, n):
        # Incrementa la métrica de ciclos efectuados en la versión optimizada.
        ciclos_con_break += 1
        # Comprueba la divisibilidad exacta.
        if (n % div == 0):
            # Cambia el estado a False para señalar que no es primo.
            primo = False
            # Cancela el resto de repeticiones del bucle 'for' para ahorrar iteraciones.
            break
    # Comprueba si se determinó que 'n' es un número primo.
    if (primo):
        # Muestra el número primo en pantalla.
        print(n)
    # Rama ejecutada si el número resultó ser compuesto.
    else:
        # Restablece la bandera 'primo' a True.
        primo = True
    # Incrementa 'n' para avanzar al próximo entero.
    n += 1
# Muestra el total de iteraciones ejecutadas en la versión optimizada con 'break'.
print('Cantidad de ciclos: ' + str(ciclos_con_break))
# Muestra la razón de rendimiento expresada como porcentaje comparativo dividiendo ambos acumuladores de iteración.
print('Se optimizó a un ' + str(ciclos_con_break / ciclos_sin_break) + '% de ciclos aplicando break')

# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
# Modifica el límite de rango aumentando el techo a 100 para probar el comportamiento de escala de la optimización.
tope_rango = 100
# Restablece la métrica de iteraciones totales sin 'break' a cero.
ciclos_sin_break = 0
# Reinicia el contador de iteración 'n' en 0.
n = 0
# Inicializa la bandera booleana 'primo' en True.
primo = True
# Bucle 'while' para evaluar candidatos hasta el nuevo tope de 100.
while (n < tope_rango):
    # Itera sobre los posibles divisores entre 2 y n-1.
    for div in range(2, n):
        # Contabiliza la iteración efectuada en la métrica sin 'break'.
        ciclos_sin_break += 1
        # Evalúa si la división entre 'n' y 'div' es exacta.
        if (n % div == 0):
            # Registra que el número es compuesto.
            primo = False
    # Muestra el número primo si la condición resulta verdadera.
    if (primo):
        # Muestra el valor primo en pantalla.
        print(n)
    # Maneja los casos donde el número resulta ser compuesto.
    else:
        # Restablece la bandera para el siguiente entero.
        primo = True
    # Avanza al siguiente número en el rango.
    n += 1
# Muestra en consola la cantidad total de ciclos ejecutados sin la sentencia 'break' para el rango de 100.
print('Cantidad de ciclos: ' + str(ciclos_sin_break))

# Restablece a cero el acumulador de iteraciones con 'break'.
ciclos_con_break = 0
# Reinicia el contador 'n' en 0 para iniciar la prueba optimizada hasta 100.
n = 0
# Inicializa la bandera 'primo' en True.
primo = True
# Bucle 'while' que recorre la secuencia hasta el tope_rango de 100.
while (n < tope_rango):
    # Itera sobre la secuencia de divisores potenciales.
    for div in range(2, n):
        # Acumula una iteración realizada en la versión optimizada.
        ciclos_con_break += 1
        # Verifica la divisibilidad exacta entre 'n' y 'div'.
        if (n % div == 0):
            # Determina que el número es compuesto.
            primo = False
            # Interrumpe la evaluación de divisores adicionales para este número.
            break
    # Imprime en consola si 'n' fue clasificado como primo.
    if (primo):
        # Muestra el número primo hallado.
        print(n)
    # Aplica la rama alternativa si el número no es primo.
    else:
        # Restablece la bandera 'primo' a True.
        primo = True
    # Incrementa 'n' para avanzar al siguiente valor dentro del rango.
    n += 1
# Imprime la cantidad total de ciclos realizados con la presencia de la sentencia 'break' hasta 100.
print('Cantidad de ciclos: ' + str(ciclos_con_break))
# Muestra el porcentaje de ciclos requeridos por la versión optimizada frente a la versión exhaustiva para un tope mayor.
print('Se optimizó a un ' + str(ciclos_con_break / ciclos_sin_break) + '% de ciclos aplicando break')
