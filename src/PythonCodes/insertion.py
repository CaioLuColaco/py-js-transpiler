def insertion_sort(arr):
    # Itera sobre todos os elementos da lista a partir do segundo elemento
    for i in range(1, len(arr)):
        key = arr[i]  # Seleciona o elemento atual para comparação
        j = i - 1     # Inicializa o índice anterior ao elemento atual

        # Move os elementos maiores que key uma posição para a direita
        # até encontrar a posição correta para inserir key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insere key na posição correta
        arr[j + 1] = key

# Exemplo de uso:
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Lista ordenada:", arr)
