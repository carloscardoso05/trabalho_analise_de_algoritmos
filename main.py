import random
import sys
from time import time
from matplotlib import pyplot as plt

# Aumenta o limite de recursão para o quicksort funcionar com vetores grandes
sys.setrecursionlimit(2 ** 16)


def quicksort(arr):
    """Implementação clássica do Quicksort com pivô no final"""
    comps = 0
    swaps = 0

    def particiona(v, esq, dir):
        nonlocal comps, swaps
        pivo = v[dir]  # Pivô no último elemento (Lomuto)
        i = esq - 1

        for j in range(esq, dir):
            comps += 1
            if v[j] <= pivo:
                i += 1
                if i != j:
                    v[i], v[j] = v[j], v[i]
                    swaps += 1

        pos_pivo = i + 1
        v[pos_pivo], v[dir] = v[dir], v[pos_pivo]
        swaps += 1
        return pos_pivo

    def ordena(v, esq, dir):
        nonlocal comps
        comps += 1
        if esq < dir:
            p = particiona(v, esq, dir)
            ordena(v, esq, p - 1)
            ordena(v, p + 1, dir)

    copia = arr.copy()
    ordena(copia, 0, len(copia) - 1)
    return copia, comps, swaps


def shellsort(lista):
    """Shellsort usando sequência de gaps original (N/2, N/4, ...)"""
    n = len(lista)
    comps = 0
    swaps = 0
    gap = n // 2

    while gap > 0:
        comps += 1
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                comps += 1
                lista[j] = lista[j - gap]
                swaps += 1
                j -= gap
            lista[j] = temp
        gap = gap // 2

    return lista, comps, swaps


def heapsort(v):
    """Heapsort usando max-heap"""
    comps = 0
    swaps = 0
    tam = len(v)

    def heapify(arr, n, i):
        nonlocal comps, swaps
        maior = i
        esq = 2 * i + 1
        dir = 2 * i + 2

        comps += 2
        if esq < n and arr[esq] > arr[maior]:
            maior = esq

        comps += 2
        if dir < n and arr[dir] > arr[maior]:
            maior = dir

        comps += 1
        if maior != i:
            arr[i], arr[maior] = arr[maior], arr[i]
            swaps += 1
            heapify(arr, n, maior)

    # Constroi heap máximo
    for i in range(tam // 2 - 1, -1, -1):
        heapify(v, tam, i)

    # Extrai elementos um por um
    for i in range(tam - 1, 0, -1):
        v[i], v[0] = v[0], v[i]
        swaps += 1
        heapify(v, i, 0)

    return v, comps, swaps


def gera_aleatorio(n):
    return [random.randint(0, 1000) for _ in range(n)]


def gera_ordenado(n):
    return list(range(n))


def gera_reverso(n):
    return list(range(n, 0, -1))


def roda_testes(tamanhos, tipo):
    resultados = []
    print(f"\nIniciando testes para vetores {tipo.replace('_', ' ')}...")

    for n in tamanhos:
        print(f"  Tamanho: {n}", end=' | ')
        # Gera vetor conforme tipo
        if tipo == 'Aleatório':
            original = gera_aleatorio(n)
        elif tipo == 'Ordenado':
            original = gera_ordenado(n)
        elif tipo == 'Inversamente ordenado':
            original = gera_reverso(n)

        # Testa cada algoritmo
        for algo in [quicksort, shellsort, heapsort]:
            comps_total = 0
            trocas_total = 0
            inicio = time()
            for _ in range(3):
                copia = original.copy()
                arr, comps, trocas = algo(copia)
                trocas_total += trocas / 3
                comps_total += comps / 3
            tempo = time() - inicio
            tempo = tempo / 3

            resultados.append((
                algo.__name__,
                n,
                tempo,
                comps,
                trocas_total
            ))
            print(f'{algo.__name__[0]}', end='')
        print()

    return resultados


def plota_graficos(dados, tipo):
    algoritmos = sorted({d[0] for d in dados})
    tamanhos = sorted({d[1] for d in dados})

    # Configura estilo do gráfico
    plt.style.use('ggplot')
    cores = {'quicksort': '#FF6B6B', 'shellsort': '#4ECDC4', 'heapsort': '#45B7D1'}

    # Plotar tempos
    plt.figure(figsize=(12, 6))
    for algo in algoritmos:
        x = [d[1] for d in dados if d[0] == algo]
        y = [d[2] for d in dados if d[0] == algo]  # Índice 2 = tempo
        plt.plot(x, y, 'o--', label=algo, color=cores[algo])
    plt.title(f'Tempo de execução - {tipo}')
    plt.xlabel('Tamanho do vetor')
    plt.ylabel('Segundos')
    plt.legend()
    plt.savefig(f'tempo_{tipo}.png', dpi=200)
    plt.close()

    # Plotar comparações
    plt.figure(figsize=(12, 6))
    for algo in algoritmos:
        x = [d[1] for d in dados if d[0] == algo]
        y = [d[3] for d in dados if d[0] == algo]  # Índice 3 = comparações
        plt.plot(x, y, 'o--', label=algo, color=cores[algo])
    plt.title(f'Comparações realizadas - {tipo}')
    plt.xlabel('Tamanho do vetor')
    plt.ylabel('Número de comparações')
    plt.legend()
    plt.savefig(f'comps_{tipo}.png', dpi=200)
    plt.close()

    # Trocas
    plt.figure(figsize=(12, 6))
    for algo in algoritmos:
        x = [d[1] for d in dados if d[0] == algo]
        y = [d[4] for d in dados if d[0] == algo]  # Índice 4 = trocas
        plt.plot(x, y, 'o--', label=algo, color=cores[algo])
    plt.title(f'Trocas realizadas - {tipo}')
    plt.xlabel('Tamanho do vetor')
    plt.ylabel('Número de trocas')
    plt.legend()
    plt.savefig(f'trocas_{tipo}.png', dpi=200)
    plt.close()


if __name__ == '__main__':
    tamanhos = list(range(0, 11000, 1000))

    # Rodar para todos os tipos de vetor
    for tipo in ['Aleatório', 'Ordenado', 'Inversamente ordenado']:
        dados = roda_testes(tamanhos, tipo)
        plota_graficos(dados, tipo)

    print("\nFim dos testes! Verifique os gráficos gerados.")
