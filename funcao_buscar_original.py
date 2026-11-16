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
    texto = TEXTO * 100

    tempoInicial = time.time()
    print(f"Posicoes ==> {busca_padrao(texto, padrao)}")
    tempoFinal = time.time()

    print(f"Total de Caractere: {len(texto)}")
    print(f"Quantidade de elementos ==> {len(busca_padrao(texto, padrao))}")
    print(f"Tempo de Execucao: {tempoFinal - tempoInicial:.2f}")

# Meta: implementar KMP ou Boyer-Moore e comparar tempos.