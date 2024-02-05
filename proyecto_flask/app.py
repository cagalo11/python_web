import sys

def pares(lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], objetivo=5): # se asignan valores por defecto
    
    resultados = [] # Se crea un vector vacío en el cual posteriormente se incluirán los resultados
    for i in range(len(lista)): # Iterando para el primer número de la suma
        for j in range(i+1, len(lista)):  # Iterando para el segundo número de la suma
            if lista[i] + lista[j] == objetivo:
                resultados.append(f"{lista[i]},{lista[j]}") # los resultados se almacenan como string
    return resultados

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Default lista
    objetivo = 5  # Default objetivo

    if len(sys.argv) > 1:
        # Se asume que la lista de entrada viene separada por comas., "1,2,3,4,5"
        lista = list(map(int, sys.argv[1].split(',')))
    if len(sys.argv) > 2: 
        objetivo = int(sys.argv[2])

    print(pares(lista, objetivo)) # se muestra la pareja que al sumar da el objetivo
