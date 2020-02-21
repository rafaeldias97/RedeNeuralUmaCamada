import numpy as np
import pandas as pd

# Carregando dados
data = pd.read_csv('./and.csv')
dfEntradas = pd.DataFrame(data, columns=['A','B'])
dfSaidas = pd.DataFrame(data, columns=['C'])
entradas = np.asarray(dfEntradas)
saidas = np.asarray(dfSaidas)

pesos = np.array([0.0, 0.0])
taxaAprendizagem = 0.1

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

def treinar():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                # print("Peso atualizado: " + str(pesos[j]))
            # print("Total de erros: " + str(erroTotal))

treinar()
v1 = int(input('A: '))
v2 = int(input('B: '))
en = np.array([v1, v2])
print(calculaSaida(en))
