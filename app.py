
def pares(lista, objetivo):
  resultados = []
  minimo_valor = min(lista)
  maximo_valor = max(lista)
  rango = maximo_valor - minimo_valor
  lista = range(minimo_valor, maximo_valor)
  for i in lista:
    for j in lista:
      if lista[i] + lista[j] == objetivo:
        resultados.append(str(lista[i]) + ","  +  str(lista[j]))
  return resultados