def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Dividir o array ao meio

        # Criar arrays vazios para as metades
        left_half = []
        right_half = []

        for i in range(mid):
            left_half.append(arr[i])
        for i in range(mid, len(arr)):
            right_half.append(arr[i])

        # Copiar dados para os arrays temporários
        for i in range(0, mid):
            left_half[i] = arr[i]

        for i in range(mid, len(arr)):
            right_half[i - mid] = arr[i]

        merge_sort(left_half)  # Recursivamente ordenar a metade esquerda
        merge_sort(right_half)  # Recursivamente ordenar a metade direita

        i = 0
        j = 0
        k = 0

        # Mesclar as duas metades ordenadas de volta no array original
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Verificar se há elementos restantes na metade esquerda
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Verificar se há elementos restantes na metade direita
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Exemplo de uso
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Array ordenado é:", arr)
