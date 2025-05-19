# Tenta todas as combinações para maior uso de capacidade

def uso_maximo_bt(tamanhos, capacidade):
    melhor = [0]

    def backtrack(i, total):
        if total > capacidade:
            return
        melhor[0] = max(melhor[0], total)
        if i == len(tamanhos):
            return
        backtrack(i+1, total + tamanhos[i])
        backtrack(i+1, total)

    backtrack(0, 0)
    return melhor[0]