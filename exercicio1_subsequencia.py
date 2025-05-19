# Exercício 1
def subsequencia(A, B):
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            j += 1
        i += 1
    return j == len(B)

A = [9, 5, 6, 3, 9, 6, 4, 7]
B = [5, 6, 4]
print(subsequencia(A, B))  # Saída: True