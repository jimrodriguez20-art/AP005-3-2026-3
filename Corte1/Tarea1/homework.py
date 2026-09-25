{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Guía Educativa: Entrada de Datos, Conversión de Tipos y Comparaciones en Python\n",
        "\n",
        "Este notebook es una guía paso a paso sobre el manejo básico de datos ingresados por el usuario mediante `input()`, la conversión explícita de tipos de datos (*type casting*) y el comportamiento de las comparaciones de valor y tipo en Python."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## 1. Captura de Datos y Conversión de Tipos (*Type Casting*)\n",
        "\n",
        "En Python, la función `input()` siempre devuelve los datos capturados en formato de cadena de texto (`str`). Para realizar operaciones matemáticas o comparaciones numéricas precisas, es necesario convertir (*cast*) estas cadenas al tipo de dato correspondiente, como números enteros (`int`) o números de punto flotante (`float`)."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Solicita al usuario que ingrese un valor por consola y lo almacena como cadena de texto (str) en la variable 'a'\n",
        "a = input(\"Enter a number: \")\n",
        "\n",
        "# Convierte (cast) el valor de 'a' de formato texto (str) a un número entero (int)\n",
        "a = int(a)\n",
        "\n",
        "# Solicita al usuario un segundo valor y lo almacena como cadena de texto (str) en la variable 'b'\n",
        "b = input(\"Enter b number: \")\n",
        "\n",
        "# Convierte (cast) el valor de 'b' de formato texto (str) a un número de punto flotante/decimal (float)\n",
        "b = float(b)\n",
        "\n",
        "# Realiza la suma de 'a' (int) y 'b' (float); Python realiza una conversión implícita de 'a' a float para operar, almacenando el resultado (float) en 'c'\n",
        "c = a + b"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## 2. Comparación de Valores Numéricos\n",
        "\n",
        "Las estructuras de control condicionales (`if-else`) permiten evaluar expresiones booleanas. En este bloque se utiliza el operador de igualdad `==` para verificar si el valor numérico contenido en `a` es equivalente al valor numérico contenido en `b`, independientemente de sus tipos de datos subyacentes."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Evalúa si el valor numérico de 'a' es igual al valor numérico de 'b'\n",
        "if a == b:\n",
        "    # Imprime \"equal\" si la condición es verdadera (True)\n",
        "    print(\"equal\")\n",
        "else:\n",
        "    # Imprime \"Different\" si la condición es falsa (False)\n",
        "    print(\"Different\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## 3. Inspección de Tipos de Datos e Impresión de Resultados\n",
        "\n",
        "La función integrada `type()` nos permite inspeccionar la clase o tipo de dato de cualquier objeto en Python. En este bloque imprimimos el tipo de dato actual de cada variable y el resultado de la suma calculada previamente."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Muestra por pantalla el tipo de dato de la variable 'a' usando la función type()\n",
        "print(\"Type of a is: \", type(a))\n",
        "\n",
        "# Muestra por pantalla el tipo de dato de la variable 'b' usando la función type()\n",
        "print(\"Type of b is: \", type(b))\n",
        "\n",
        "# Imprime la etiqueta \"c = \" seguida del valor numérico resultante almacenado en 'c'\n",
        "print(\"c = \", c)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## 4. Comparación Estricta de Tipos de Datos\n",
        "\n",
        "Además de comparar valores, se pueden comparar directamente los tipos de datos retornados por `type()`. En este caso particular, como `a` fue convertido a `int` y `b` a `float`, la condición evaluará siempre `False`.\n",
        "\n",
        "> **Nota técnica:** En el código original, esta condición siempre será falsa porque un tipo `int` y un tipo `float` son clases distintas en la jerarquía de tipos de Python (`int != float`), aunque sus valores numéricos puedan ser equivalentes (por ejemplo, `5` y `5.0`)."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Compara si la clase/tipo de la variable 'a' es idéntica a la clase/tipo de la variable 'b'\n",
        "if type(a) == type(b):\n",
        "    # Se ejecutaría si ambas variables compartieran exactamente el mismo tipo de dato\n",
        "    print(\"a and b are of the same type\")\n",
        "else:\n",
        "    # Se ejecuta cuando las variables pertenecen a tipos de datos diferentes (ej. int vs float)\n",
        "    print(\"a and b are of different type\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## Conclusión\n",
        "\n",
        "En este ejercicio se abordaron tres conceptos fundamentales del lenguaje Python:\n",
        "\n",
        "1. **Entrada de datos y casting:** La función `input()` retorna siempre `str`, haciendo obligatoria la conversión explícita (`int()`, `float()`) para realizar cálculos aritméticos.\n",
        "2. **Coerción implícita de tipos:** Al sumar un entero (`int`) con un flotante (`float`), Python promueve automáticamente el resultado al tipo más amplio (`float`) para evitar pérdida de precisión.\n",
        "3. **Diferencia entre valor y tipo:** El operador `==` sobre variables compara equivalencia de **valores** (donde `5 == 5.0` es `True`), mientras que la comparación entre resultados de `type()` evalúa la **identidad del tipo de dato** (donde `type(int) == type(float)` es `False`)."
      ]
    }
  ],
  "metadata": {
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 2
}
