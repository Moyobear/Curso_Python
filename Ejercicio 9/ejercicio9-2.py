from functools import reduce


def filtraReduce(lista):
    resultado = list(filter((lambda item: item % 2), lista))
    resultado = reduce((lambda acum, next: acum + next), resultado)
    return resultado


lista = list(range(50))

print(filtraReduce(lista))
