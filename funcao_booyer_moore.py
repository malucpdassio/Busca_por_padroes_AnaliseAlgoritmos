import time
from textoExemplo import TEXTO

def busca_padrao(texto, padrao):
    n, m = len(texto), len(padrao)
    if m == 0 or m > n:
        return []
        
    # Construção da tabela de deslocamento (Horspool)
    # Define o salto com base na distância de cada caractere até o final do padrão
    tabela = {}
    for i in range(m - 1):
        tabela[padrao[i]] = m - 1 - i
        
    ocorrencias = []
    s = 0  # Deslocamento do padrão em relação ao texto
    
    while s <= n - m:
        j = m - 1
        
        # Compara da direita para a esquerda
        while j >= 0 and padrao[j] == texto[s + j]:
            j -= 1
            
        # Se encontrou o padrão completo
        if j < 0:
            ocorrencias.append(s)
            s += 1  # Avança uma posição para continuar a procurar outras ocorrências
        else:
            # Salto inteligente baseado no caractere do texto alinhado com o fim do padrão
            char_alinhado = texto[s + m - 1]
            s += tabela.get(char_alinhado, m)

    return ocorrencias


if __name__ == "__main__":

    padrao = "Python"
    texto = TEXTO*100

    tempoInicial = time.time()
    print(f"Posicoes ==> {busca_padrao(texto, padrao)}")
    tempoFinal = time.time()

    print(f"Total de Caractere: {len(texto)}")
    print(f"Quantidade de elementos ==> {len(busca_padrao(texto, padrao))}")
    print(f"Tempo de Execucao: {tempoFinal - tempoInicial:.2f}")