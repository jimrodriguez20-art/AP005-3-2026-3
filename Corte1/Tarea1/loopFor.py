# Importa el módulo 'time' de la biblioteca estándar de Python; proporciona funciones relacionadas con el tiempo y retardos en la ejecución.
import time

# Declara la variable 'cadena' e inicializa un objeto de tipo texto (str) con el valor 'Python'; define la secuencia a recorrer.
cadena = 'Python'

# Inicia un bucle 'for' que itera secuencialmente sobre cada carácter de 'cadena', asignándolo a la variable 'letra'; controla la lectura carácter por carácter.
for letra in cadena:
    # Compara si el carácter actual contenido en 'letra' es exactamente igual al string 't'; actúa como filtro condicional de omisión.
    if letra == 't':
        # Salta de inmediato el resto de las instrucciones del cuerpo del bucle y avanza al siguiente carácter; excluye la letra 't' del procesamiento.
        continue
    # Imprime en la consola el carácter actual almacenado en 'letra'; muestra únicamente las letras que no fueron omitidas por la sentencia 'continue'.
    print(letra)
    # Pausa la ejecución del programa durante 1 segundo usando time.sleep(); genera un intervalo de tiempo visible entre la salida de cada carácter.
    time.sleep(1)
