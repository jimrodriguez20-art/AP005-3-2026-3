# Inicia un bucle que iterará la variable 'i' desde 100 hasta 300 (el límite superior 301 es excluyente); define el universo de números a evaluar.
for i in range(100, 301):
    # Evalúa con el operador módulo (%) si 'i' NO es divisible entre 12 (residuo diferente de cero); actúa como filtro lógico principal del algoritmo.
    if (i % 12) != 0:
        # Salta el resto del cuerpo del bucle y pasa inmediatamente a la siguiente iteración; descarta los números que no cumplen el criterio de divisibilidad.
        continue
    # Imprime en consola el valor actual de 'i'; solo se ejecuta si la condición previa fue falsa, mostrando los números que sí son múltiplos de 12.
    print(i)
