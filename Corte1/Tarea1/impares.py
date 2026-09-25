{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Guía Educativa: Bucles Iterativos, Operadores Aritméticos y Control de Flujo en Python\n",
        "\n",
        "Este notebook presenta una guía paso a paso sobre el uso de bucles `for`, el operador módulo (`%`), la exponenciación, el *type casting* (conversión de tipos de datos) y la validación de condiciones de ejecución mediante estructuras `if-else`."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## 1. Identificación de Números Pares e Impares con Módulo (`%`)\n",
        "\n",
        "En este bloque se itera sobre un rango de números enteros del 1 al 20. En cada iteración, se calcula el residuo de la división entera entre 2 utilizando el operador módulo (`%`). Si el residuo es igual a `0`, el número es par (*even*); de lo contrario, es impar (*odd*)."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Inicia un bucle 'for' que iterará desde i = 1 hasta i = 20 (el límite superior 21 es exclusivo)\n",
        "for i in range(1, 21):\n",
        "    # Calcula el residuo de la división de 'i' entre 2 usando el operador módulo (%)\n",
        "    residual = i % 2\n",
        "    \n",
        "    # Evalúa si el residuo es igual a 0 para determinar si el número es par\n",
        "    if residual == 0:\n",
        "        # Imprime una cadena con formato f-string indicando que el número es par\n",
        "        print(f'{i} is even')\n",
        "    else:\n",
        "        # Concatena la representación en texto de 'i' con la cadena ' is odd' para los números impares\n",
        "        print(str(i) + ' is odd')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## 2. Cálculo de Potencias mediante Exponenciación (`**`)\n",
        "\n",
        "En este bloque se itera en un rango de 0 a 5. Dentro del cuerpo del bucle, se eleva la variable de control al cubo utilizando el operador de exponenciación (`**`) y se imprime el resultado en cada ciclo."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Inicia un bucle 'for' que itera desde i = 0 hasta i = 5 (el límite superior 6 no se incluye)\n",
        "for i in range(0, 6):\n",
        "    # Eleva el valor de 'i' al cubo (potencia 3) usando el operador de exponenciación (**)\n",
        "    result = i ** 3\n",
        "    \n",
        "    # Muestra en consola el valor resultante del cálculo\n",
        "    print(result)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## 3. Captura de Entrada e Interpretación de Tipos de Datos (*Casting*)\n",
        "\n",
        "Aquí se solicita una entrada al usuario mediante `input()`, la cual retorna una cadena de texto (`str`). Posteriormente, se realiza una doble conversión de tipo (*casting*): primero a `float` y luego a `int` (lo cual trunca cualquier parte decimal ingresada) antes de inspeccionar su tipo."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Solicita al usuario ingresar un valor numérico por consola y lo guarda como cadena (str)\n",
        "times = input(\"Enter a number of times: \")\n",
        "\n",
        "# Convierte la cadena ingresada a un número de punto flotante (float)\n",
        "times = float(times)\n",
        "\n",
        "# Convierte el número flotante a un número entero (int), truncando la parte decimal si existiera\n",
        "times = int(times)\n",
        "\n",
        "# Muestra en consola la clase o tipo de dato resultante de la variable 'times'\n",
        "print(type(times))\n",
        "\n",
        "# Imprime el valor final procesado almacenado en 'times'\n",
        "print(times)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## 4. Control de Flujo Condicional e Iteración Dinámica\n",
        "\n",
        "En esta sección final se evalúa el valor entero de `times`. Si es igual a `0`, la estructura condicional interrumpe la acción imprimiendo un mensaje. Si es diferente de `0`, se ejecuta un bucle `for` que genera una secuencia incremental de números desde `1` hasta `times`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Evalúa si el número de repeticiones ingresado por el usuario es igual a 0\n",
        "if times == 0:\n",
        "    # Muestra un mensaje en pantalla e ignora la ejecución del bucle si times es 0\n",
        "    print(\"Don't do anything\")\n",
        "else:\n",
        "    # Ejecuta un bucle desde 1 hasta 'times' inclusive (sumando 1 al límite superior de range)\n",
        "    for i in range(1, times + 1):\n",
        "        # Imprime el contador 'i' de la iteración actual\n",
        "        print(\"i = \", i)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## Conclusión\n",
        "\n",
        "En esta guía práctica se integraron varios conceptos fundamentales de la programación en Python:\n",
        "\n",
        "1. **Operadores Aritméticos:** El uso de `%` (módulo) permite determinar la paridad de un número analizando el residuo de su división entera, mientras que `**` facilita operaciones de potencia.\n",
        "2. **Transformación de Tipos (*Type Casting*):** Se analizó la conversión desde `str` hacia `float` e `int`. Es relevante notar que transformar un `float` a `int` trunca los decimales sin redondear.\n",
        "3. **Estructuras Condicionales y Iterativas:** La combinación de `if-else` con la función `range()` permite controlar dinámicamente cuántas veces se ejecuta un bloque de código según los parámetros ingresados por el usuario."
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
