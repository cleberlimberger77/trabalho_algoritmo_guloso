# Exercício 2
# Determina o número mínimo de reabastecimentos

def min_reabastecimentos(distancias, autonomia):
    posicoes = [0] + distancias
    reabastecimentos = 0
    atual = 0

    while atual < len(posicoes) - 1:
        proximo = atual
        while (proximo + 1 < len(posicoes)) and (posicoes[proximo + 1] - posicoes[atual] <= autonomia):
            proximo += 1
        if proximo == atual:
            return -1  # Não é possível continuar
        atual = proximo
        if atual < len(posicoes) - 1:
            reabastecimentos += 1
    return reabastecimentos

postos = [100, 200, 300, 400, 500]
autonomia = 200
print(min_reabastecimentos(postos, autonomia)) 