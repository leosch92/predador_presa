from copy import copy


def atualiza_lista(lista, novo):
    lista_copia = []
    for j in range(len(lista) - 1):
        lista_copia.append(lista[j + 1])
    lista_copia.append(novo)
    return copy(lista_copia)