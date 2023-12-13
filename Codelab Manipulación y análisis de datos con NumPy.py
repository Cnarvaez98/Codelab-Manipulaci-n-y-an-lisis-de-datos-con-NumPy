import numpy as np

def ej_1_get_array() -> np.ndarray:
    temperaturas = np.array([25, 30, 27, 22, 29, 31, 26, 28])
    return temperaturas

def ej_1_calculate_stats(temperaturas: np.ndarray):
    # Calcula la media y la desviación estándar
    media = np.mean(temperaturas)
    desviacion = np.std(temperaturas)

    # Convierte a grados Fahrenheit
    temperaturas_fahrenheit = temperaturas * 9/5 + 32

    # Encuentra la temperatura máxima y mínima
    temp_max = np.max(temperaturas_fahrenheit)
    temp_min = np.min(temperaturas_fahrenheit)

    # Encuentra las diferencias con la media
    diferencias = temperaturas - media

    # Calcula el cuadrado de cada diferencia
    diferencias_cuadrado = np.square(diferencias)

    # Calcula la suma de cuadrados y la raíz cuadrada de la suma
    suma_cuadrados = np.sum(diferencias_cuadrado)
    raiz_suma_cuadrados = np.sqrt(suma_cuadrados)

    return media, desviacion, temperaturas_fahrenheit, temp_max, temp_min, diferencias, diferencias_cuadrado, suma_cuadrados, raiz_suma_cuadrados

# Ejemplo de uso:
temperaturas = ej_1_get_array()
resultados = ej_1_calculate_stats(temperaturas)
print(resultados)
