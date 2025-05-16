def obtener_indice(lista : list, elemento : int | float | str)-> int:
    """
    La funcion retorna el indice de la del elemento buscado. si este no existe retorna -1

    """
    indice = 0
    for i in lista:
        if i == elemento:
            return indice
        indice += 1
    return -1