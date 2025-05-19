# Algoritmo de mochila 0/1 com programacao dinâmica

def mochila(tamanhos, estrelas, capacidade):
    n = len(tamanhos)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacidade + 1):
            if tamanhos[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - tamanhos[i-1]] + estrelas[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacidade]