import sys

def pares(lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], objetivo=5):
    
    resultados = []
    for i in range(len(lista)):
        for j in range(i+1, len(lista)): 
            if lista[i] + lista[j] == objetivo:
                resultados.append(f"{lista[i]},{lista[j]}")
    return resultados

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Default list
    objetivo = 5  # Default objetivo

    if len(sys.argv) > 1:
        # Assuming command-line 'lista' as comma-separated values, e.g., "1,2,3,4,5"
        lista = list(map(int, sys.argv[1].split(',')))
    if len(sys.argv) > 2:
        objetivo = int(sys.argv[2])

    print(pares(lista, objetivo))
