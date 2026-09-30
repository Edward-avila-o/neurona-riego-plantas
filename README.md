# Neurona Artificial para el Riego de Plantas

## Descripción del proyecto

En este proyecto se desarrolló una neurona artificial que permite determinar si una planta necesita ser regada utilizando dos datos de entrada:

- Humedad del suelo.
- Temperatura ambiental.

La neurona analiza estos valores y genera una respuesta de tipo binaria:

- 1: La planta necesita riego.
- 0: La planta no necesita riego.

Para realizar el entrenamiento se utilizaron conceptos como pesos, sesgo, normalización, función sigmoide, tasa de aprendizaje y épocas de entrenamiento.

Los datos utilizados son únicamente para fines académicos y permiten observar el funcionamiento de una neurona artificial aplicada a un problema diferente a una compuerta lógica.

---

## Herramientas utilizadas

- Python.
- NumPy.
- UV para manejar las dependencias del proyecto.

---

## Ejecución del proyecto

Para instalar las dependencias del proyecto:

```bash
uv sync
```

Para ejecutar la neurona:

```bash
uv run main.py
```

---

## Funcionamiento

La neurona utiliza dos entradas principales:

| Entrada | Descripción |
|---|---|
| X1 | Humedad del suelo (%) |
| X2 | Temperatura ambiental (°C) |

Antes de realizar el entrenamiento se aplicó una normalización de los datos para que las dos variables trabajaran en una escala similar.

La neurona calcula una suma ponderada utilizando los pesos y el sesgo, posteriormente aplica la función sigmoide para obtener una probabilidad entre 0 y 1.

Finalmente, utilizando un umbral de 0.5 se obtiene la decisión:

- Mayor o igual a 0.5 → Regar.
- Menor a 0.5 → No regar.

---

## Parámetros utilizados

Para el entrenamiento se utilizaron los siguientes valores:

| Parámetro | Valor |
|---|---|
| Función de activación | Sigmoide |
| Tasa de aprendizaje | 0.5 |
| Épocas | 10000 |
| Umbral | 0.5 |

---

## Resultados obtenidos

Después de entrenar la neurona se obtuvieron los siguientes resultados:

| Elemento | Resultado |
|---|---|
| Peso humedad | -33.27729484064782 |
| Peso temperatura | 0.3467428040501668 |
| Sesgo | 14.748383350549059 |
| Error final | 0.005378389647029539 |
| Datos clasificados correctamente | 10/10 |

La neurona logró clasificar correctamente todos los ejemplos utilizados durante el entrenamiento.

---

## Interpretación de resultados

El peso de la humedad obtuvo un valor negativo, lo que indica que cuando aumenta la humedad del suelo disminuye la posibilidad de necesitar riego.

El peso de la temperatura obtuvo un valor positivo, indicando que cuando la temperatura aumenta también puede aumentar la necesidad de agua de la planta.

---

## Pruebas con nuevos datos

Después del entrenamiento se probaron diferentes condiciones:

| Humedad | Temperatura | Probabilidad | Decisión |
|---|---|---|---|
|75%|30°C|0.000|No regar|
|45%|34°C|0.502|Regar|
|25%|22°C|0.999|Regar|
|50%|25°C|0.152|No regar|
|30%|40°C|0.994|Regar|

---

# Análisis

## 1. ¿Por qué fue necesario normalizar la humedad y la temperatura?

Fue necesario porque las dos variables tenían diferentes escalas. La humedad estaba representada entre 0 y 100, mientras que la temperatura trabajaba aproximadamente entre 0 y 50. Al normalizar los valores, la neurona puede procesar mejor las entradas.

## 2. ¿En qué operaciones se utilizó X_normalizado y para qué se conservó X?

X_normalizado se utilizó durante el entrenamiento para realizar los cálculos de la neurona y actualizar los pesos.

La variable X se mantuvo con los valores originales para poder interpretar los datos más fácilmente.

## 3. ¿Qué ocurrió al utilizar solamente 100 épocas?

La neurona tuvo menos iteraciones para aprender, por lo que el ajuste de los pesos fue menor y los resultados pueden tener más errores.

## 4. ¿Más épocas siempre produjeron una mejora importante?

No siempre. Después de suficientes épocas la mejora comienza a ser menor porque la neurona ya encontró valores adecuados para sus pesos.

## 5. ¿Qué efecto tuvo una tasa de aprendizaje pequeña?

La neurona aprendió más lentamente porque los cambios realizados sobre los pesos eran pequeños.

## 6. ¿Qué efecto tuvo una tasa de aprendizaje alta o muy alta?

Los cambios en los pesos fueron mayores, permitiendo aprender más rápido, pero una tasa demasiado alta puede generar inestabilidad.

## 7. ¿Qué representa el signo del peso de la humedad?

El signo negativo indica que existe una relación inversa entre humedad y riego. Cuando hay más humedad, la planta necesita menos agua.

## 8. ¿Qué representa el signo del peso de temperatura?

El signo positivo indica que una temperatura mayor puede aumentar la necesidad de riego.

## 9. ¿Por qué una probabilidad debe convertirse en 0 o 1 mediante un umbral?

Porque la función sigmoide entrega una probabilidad, pero el sistema necesita una decisión final que indique si se debe regar o no.

## 10. ¿Qué limitaciones tiene esta neurona?

La neurona solamente utiliza humedad y temperatura. Para un sistema real sería necesario considerar otros factores como tipo de planta, iluminación, humedad del ambiente y características del suelo.

---

## Conclusión

Con este proyecto se pudo observar cómo una neurona artificial puede aprender una relación entre diferentes datos de entrada y una salida esperada.

El modelo logró clasificar correctamente los ejemplos utilizados, demostrando el funcionamiento básico del aprendizaje supervisado.

Aunque funciona correctamente con los datos de prueba, es importante recordar que se trata de un modelo académico y no de un sistema real de riego automático.

