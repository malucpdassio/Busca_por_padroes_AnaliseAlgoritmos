def busca_padrao(texto, padrao):
    n, m = len(texto), len(padrao)
    ocorrencias = []
    for i in range(n - m + 1):
        if texto[i:i+m] == padrao:
            ocorrencias.append(i)
    return ocorrencias

# Meta: implementar KMP ou Boyer-Moore e comparar tempos.