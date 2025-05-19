# Tenta todas as combinações com backtracking para max arquivos

def max_arquivos_bt(tamanhos, capacidade):
    melhor = [0]

    def backtrack(i, total, count):
        if total > capacidade:
            return
        melhor[0] = max(melhor[0], count)
        if i == len(tamanhos):
            return
        backtrack(i+1, total + tamanhos[i], count + 1)
        backtrack(i+1, total, count)

    backtrack(0, 0, 0)
    return melhor[0]