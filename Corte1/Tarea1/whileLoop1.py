# Inicia un bucle 'for' que intenta iterar la variable 'i' desde 1 hasta 5 (el 6 es excluyente); actúa como la estructura de control externa del script.
for i in range(1, 6):
    # Inicia un bucle 'while' que continuará ejecutándose mientras la variable 'i' sea menor o igual a 4; controla el incremento secundario de 'i'.
    while i <= 4:
        # Incrementa en 1 el valor actual de la variable 'i'; modifica la variable de iteración compartida con el bucle 'for'.
        i += 1
        # Imprime en la consola el valor recién actualizado de 'i'; muestra los números generados durante la ejecución del 'while'.
        print(i)
    # Interrumpe y cancela inmediatamente el bucle 'for' externo en su primera iteración; evita que el bucle 'for' continúe con el resto de la secuencia (2 a 5).
    break
