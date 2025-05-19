# Algoritmo guloso por estrelas (ordem decrescente de R[i])

def guloso_estrelas(tamanhos, estrelas, capacidade):
    itens = list(zip(tamanhos, estrelas))
    itens.sort(key=lambda x: -x[1])  # ordena por estrelas decrescente
    total_estrelas, total_tamanho = 0, 0
    for t, r in itens:
        if total_tamanho + t <= capacidade:
            total_tamanho += t
            total_estrelas += r
    return total_estrelas

tamanhos = [5, 4, 6]
estrelas = [2, 5, 4]
capacidade = 10
print(guloso_estrelas(tamanhos, estrelas, capacidade))  # Pode dar 9 (4+5), mas ideal é 7 (5+2)