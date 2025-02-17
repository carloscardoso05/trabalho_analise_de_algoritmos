import random
import sys
import time

import matplotlib.pyplot as plt

sys.setrecursionlimit(2 ** 16)


# Quick Sort com partição tradicional
def quick_sort(arr):
    comparacoes = 0
    trocas = 0

    def particao(arr, low, high):
        nonlocal comparacoes, trocas
        pivo = arr[high]  # Escolhe o último elemento como pivô
        i = low - 1  # Índice do menor elemento

        for j in range(low, high):
            comparacoes += 1
            if arr[j] <= pivo:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                trocas += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        trocas += 1
        return i + 1

    def _quick_sort(arr, low, high):
        nonlocal comparacoes, trocas
        if low < high:
            pi = particao(arr, low, high)  # Índice da partição
            _quick_sort(arr, low, pi - 1)  # Ordena a parte esquerda
            _quick_sort(arr, pi + 1, high)  # Ordena a parte direita

    _quick_sort(arr, 0, len(arr) - 1)
    return arr, comparacoes, trocas


# Shell Sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    comparacoes = 0
    trocas = 0

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparacoes += 1
                arr[j] = arr[j - gap]
                trocas += 1
                j -= gap
            arr[j] = temp
            if j >= gap:
                comparacoes += 1
        gap = gap // 2

    return arr, comparacoes, trocas


# Heap Sort
def heap_sort(arr):
    comparacoes = 0
    trocas = 0

    def heapify(arr, n, i):
        nonlocal comparacoes, trocas
        maior = i
        esquerda = 2 * i + 1
        direita = 2 * i + 2

        if esquerda < n and arr[i] < arr[esquerda]:
            comparacoes += 1
            maior = esquerda

        if direita < n and arr[maior] < arr[direita]:
            comparacoes += 1
            maior = direita

        if maior != i:
            arr[i], arr[maior] = arr[maior], arr[i]
            trocas += 1
            heapify(arr, n, maior)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        trocas += 1
        heapify(arr, i, 0)

    return arr, comparacoes, trocas


# Funções para gerar vetores
def vetor_aleatorio(tamanho):
    return [random.randint(0, 1000) for _ in range(tamanho)]


def vetor_ordenado(tamanho):
    return [i for i in range(tamanho)]


def vetor_inversamente_ordenado(tamanho):
    return [i for i in range(tamanho, 0, -1)]


# Função para testar os algoritmos
def testar_algoritmos(tamanhos_vetores, tipo_vetor):
    resultados = []

    for tamanho in tamanhos_vetores:
        if tipo_vetor == "aleatorio":
            arr = vetor_aleatorio(tamanho)
        elif tipo_vetor == "ordenado":
            arr = vetor_ordenado(tamanho)
        elif tipo_vetor == "inversamente_ordenado":
            arr = vetor_inversamente_ordenado(tamanho)

        # Quick Sort
        inicio = time.time()
        arr_ordenado, comparacoes, trocas = quick_sort(arr.copy())
        tempo_quick = time.time() - inicio
        resultados.append(('Quick Sort', tamanho, tempo_quick, comparacoes, trocas))

        # Shell Sort
        inicio = time.time()
        arr_ordenado, comparacoes, trocas = shell_sort(arr.copy())
        tempo_shell = time.time() - inicio
        resultados.append(('Shell Sort', tamanho, tempo_shell, comparacoes, trocas))

        # Heap Sort
        inicio = time.time()
        arr_ordenado, comparacoes, trocas = heap_sort(arr.copy())
        tempo_heap = time.time() - inicio
        resultados.append(('Heap Sort', tamanho, tempo_heap, comparacoes, trocas))

    return resultados


# Função para plotar os resultados
def plotar_resultados(resultados, tipo_vetor):
    tamanhos = sorted(list(set(resultado[1] for resultado in resultados)))
    algoritmos = ['Quick Sort', 'Shell Sort', 'Heap Sort']

    # Tempo de execução
    plt.figure(figsize=(10, 5))
    for algoritmo in algoritmos:
        tempos = [resultado[2] for resultado in resultados if resultado[0] == algoritmo]
        plt.plot(tamanhos, tempos, label=algoritmo)
    plt.xlabel('Tamanho do Vetor')
    plt.ylabel('Tempo de Execução (s)')
    plt.title(f'Tempo de Execução dos Algoritmos de Ordenação ({tipo_vetor})')
    plt.legend()
    plt.show()

    # Número de comparações
    plt.figure(figsize=(10, 5))
    for algoritmo in algoritmos:
        comparacoes = [resultado[3] for resultado in resultados if resultado[0] == algoritmo]
        plt.plot(tamanhos, comparacoes, label=algoritmo)
    plt.xlabel('Tamanho do Vetor')
    plt.ylabel('Número de Comparações')
    plt.title(f'Número de Comparações dos Algoritmos de Ordenação ({tipo_vetor})')
    plt.legend()
    plt.show()

    # Número de trocas
    plt.figure(figsize=(10, 5))
    for algoritmo in algoritmos:
        trocas = [resultado[4] for resultado in resultados if resultado[0] == algoritmo]
        plt.plot(tamanhos, trocas, label=algoritmo)
    plt.xlabel('Tamanho do Vetor')
    plt.ylabel('Número de Trocas')
    plt.title(f'Número de Trocas dos Algoritmos de Ordenação ({tipo_vetor})')
    plt.legend()
    plt.show()


# Testando os algoritmos
tamanhos_vetores = [100, 500, 1000, 5000, 10000]

# Testes com vetores aleatórios
print("Testes com vetores aleatórios:")
resultados_aleatorios = testar_algoritmos(tamanhos_vetores, "aleatorio")
plotar_resultados(resultados_aleatorios, "Vetores Aleatórios")

# Testes com vetores ordenados
print("Testes com vetores ordenados:")
resultados_ordenados = testar_algoritmos(tamanhos_vetores, "ordenado")
plotar_resultados(resultados_ordenados, "Vetores Ordenados")

# Testes com vetores inversamente ordenados
print("Testes com vetores inversamente ordenados:")
resultados_inversamente_ordenados = testar_algoritmos(tamanhos_vetores, "inversamente_ordenado")
plotar_resultados(resultados_inversamente_ordenados, "Vetores Inversamente Ordenados")
