#METODO DE LA BURBUJA
#METODO RADIX
#BUSQUEDA BINARIA
#BUSQUEDA SECUENCIAL
#METODO QUICK SORT

#Enrique Martinez Luna

import random

def main():
    lista = []
    for i in range(10):  # Generar lista de 10 números aleatorios
        lista.append(random.randint(0, 100))
    longitud = len(lista)
    print("Lista original:", lista)

    # Métodos de ordenación
    Bubble_sort(lista.copy(), longitud)
    Selection_sort(lista.copy(), longitud)
    Insertion_sort(lista.copy(), longitud)

    # Métodos avanzados de ordenación
    lista_quick = Quick_sort(lista.copy())
    print("Lista ordenada con Quick Sort:", lista_quick)
    
    lista_merge = Merge_sort(lista.copy())
    print("Lista ordenada con Merge Sort:", lista_merge)
    
    Heap_sort(lista.copy())

    lista_radix = lista.copy()
    radix_sort(lista_radix)
    print("Lista ordenada con Radix Sort:", lista_radix)

    # Métodos de búsqueda
    elemento_a_buscar = random.choice(lista)
    print("Buscando elemento:", elemento_a_buscar)

    resultado_binaria = busqueda_binaria(lista_quick, elemento_a_buscar)
    print("Resultado búsqueda binaria:", "Encontrado en posición" if resultado_binaria != -1 else "No encontrado", resultado_binaria)

    resultado_secuencial = busqueda_secuencial(lista, elemento_a_buscar)
    print("Resultado búsqueda secuencial:", "Encontrado en posición" if resultado_secuencial != -1 else "No encontrado", resultado_secuencial)


# Algoritmos de ordenación

def swap(lista, i, j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def Bubble_sort(lista, longitud):
    for i in range(longitud):
        for j in range(longitud - i - 1):
            if lista[j] > lista[j + 1]:
                swap(lista, j, j + 1)
    print("Lista ordenada con Bubble Sort:", lista)

def Selection_sort(lista, longitud):
    for i in range(longitud):
        min_idx = i
        for j in range(i + 1, longitud):
            if lista[j] < lista[min_idx]:
                min_idx = j
        swap(lista, i, min_idx)
    print("Lista ordenada con Selection Sort:", lista)

def Insertion_sort(lista, longitud):
    for i in range(1, longitud):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    print("Lista ordenada con Insertion Sort:", lista)

# Algoritmo Quick Sort (O(n log n))
def Quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    left = [x for x in lista if x < pivot]
    middle = [x for x in lista if x == pivot]
    right = [x for x in lista if x > pivot]
    return Quick_sort(left) + middle + Quick_sort(right)

# Algoritmo Merge Sort (O(n log n))
def Merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    left = Merge_sort(lista[:mid])
    right = Merge_sort(lista[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Algoritmo Heap Sort (O(n log n))
def Heap_sort(lista):
    def heapify(lista, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and lista[i] < lista[left]:
            largest = left
        if right < n and lista[largest] < lista[right]:
            largest = right
        if largest != i:
            swap(lista, i, largest)
            heapify(lista, n, largest)

    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    for i in range(n - 1, 0, -1):
        swap(lista, 0, i)
        heapify(lista, i, 0)

    print("Lista ordenada con Heap Sort:", lista)


# Algoritmo Radix Sort (O(nk) para números enteros)
def radix_sort(lista):
    def counting_sort(lista, exp):
        n = len(lista)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = lista[i] // exp
            count[index % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            index = lista[i] // exp
            output[count[index % 10] - 1] = lista[i]
            count[index % 10] -= 1
            i -= 1
        for i in range(n):
            lista[i] = output[i]

    max_val = max(lista)
    exp = 1
    while max_val // exp > 0:
        counting_sort(lista, exp)
        exp *= 10

# Algoritmos de búsqueda

def busqueda_binaria(lista, elemento):
    low = 0
    high = len(lista) - 1
    while low <= high:
        mid = (low + high) // 2
        if lista[mid] == elemento:
            return mid
        elif lista[mid] < elemento:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Elemento no encontrado

def busqueda_secuencial(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1  # Elemento no encontrado


main()
