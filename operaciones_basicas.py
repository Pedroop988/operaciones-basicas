"""
Módulo operaciones_basicas.py
Este módulo define clases para realizar operaciones matemáticas básicas y calcular promedios.
"""

class OperacionesBasicas:
    """Clase que realiza operaciones básicas como suma y resta."""

    def __init__(self):
        """Inicializa la clase con un atributo resultado en 0."""
        self.resultado = 0

    def sumar(self, a, b):
        """Suma dos números y almacena el resultado."""
        self.resultado = a + b

    def restar(self, a, b):
        """Resta dos números y almacena el resultado."""
        self.resultado = a - b

    def obtener_resultado(self):
        """Retorna el resultado de la última operación."""
        return self.resultado


class CalculadoraPromedio:
    """Clase para calcular el promedio de una lista de valores."""

    def __init__(self, valores):
        """Inicializa la clase con una lista de valores."""
        self.valores = valores

    def calcular_promedio(self):
        """Calcula el promedio de los valores almacenados."""
        suma_total = sum(self.valores)
        return suma_total / len(self.valores)

    def contar_elementos(self):
        """Devuelve la cantidad de elementos en la lista de valores."""
        return len(self.valores)


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM1 = 10
NUM2 = 20

# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM1, NUM2)
    print(f"El resultado de la suma es: {operaciones.obtener_resultado()}")

    operaciones.restar(NUM1, NUM2)
    print(f"El resultado de la resta es: {operaciones.obtener_resultado()}")

    # Usar la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    promedio_resultado = calculadora_promedio.calcular_promedio()
    print(f"El promedio de los números es: {promedio_resultado}")
