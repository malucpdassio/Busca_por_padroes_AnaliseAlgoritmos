import time
from textoExemplo import TEXTO

def busca_padrao(texto, padrao):
    
    n, m = len(texto), len(padrao)
    ocorrencias = []
    for i in range(n - m + 1):
        if texto[i:i+m] == padrao:
            ocorrencias.append(i)

    
    return ocorrencias


if __name__ == "__main__":

    padrao = "Python"

    tempoInicial = time.time()
    print(busca_padrao(TEXTO, padrao))
    tempoFinal = time.time()

    print(f"Tempo de Execucao: {tempoFinal - tempoInicial}")

# Meta: implementar KMP ou Boyer-Moore e comparar tempos.