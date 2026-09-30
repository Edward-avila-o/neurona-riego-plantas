import numpy as np


# Datos de entrenamiento
X = np.array([
    [80,18],
    [70,22],
    [65,28],
    [55,25],
    [50,32],
    [40,30],
    [35,25],
    [30,32],
    [20,35],
    [10,38]
], dtype=float)


y = np.array([
    [0],
    [0],
    [0],
    [0],
    [0],
    [1],
    [1],
    [1],
    [1],
    [1]
], dtype=float)


# Normalización
escala = np.array([100,50])
X_normalizado = X / escala


# Función sigmoide
def sigmoide(z):
    return 1/(1+np.exp(-z))


# Entrenamiento
pesos = np.zeros((2,1))
sesgo = 0

tasa_aprendizaje = 0.5
epocas = 10000


for epoca in range(epocas):

    z = np.dot(X_normalizado,pesos)+sesgo

    probabilidad = sigmoide(z)

    error = y - probabilidad

    gradiente = error*(probabilidad*(1-probabilidad))

    gradiente_pesos = np.dot(
        X_normalizado.T,
        gradiente
    )

    gradiente_sesgo = np.sum(gradiente)


    pesos += tasa_aprendizaje * gradiente_pesos
    sesgo += tasa_aprendizaje * gradiente_sesgo



# Resultado entrenamiento

prediccion = (probabilidad >= 0.5).astype(int)

error_final = np.mean((y-probabilidad)**2)


print("\nRESULTADO DEL ENTRENAMIENTO")
print("----------------------------")

print("Peso humedad:", pesos[0][0])
print("Peso temperatura:", pesos[1][0])
print("Sesgo:", sesgo)
print("Error final:", error_final)
print("Aciertos:", np.sum(prediccion==y),"/10")



# Pruebas nuevas

datos_nuevos = np.array([
    [75,30],
    [45,34],
    [25,22],
    [50,25],
    [30,40]
],dtype=float)


datos_nuevos = datos_nuevos / escala


z = np.dot(datos_nuevos,pesos)+sesgo

probabilidades = sigmoide(z)

decisiones = (probabilidades>=0.5).astype(int)


print("\nPRUEBAS NUEVAS")
print("----------------")

for i in range(len(datos_nuevos)):

    print(
        "Probabilidad:",
        round(float(probabilidades[i][0]),3),
        "Decision:",
        "Regar" if decisiones[i][0]==1 else "No regar"
    )