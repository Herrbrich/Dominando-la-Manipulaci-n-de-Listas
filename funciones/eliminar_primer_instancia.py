

def eliminar_primer_instancia(lista: list, elemento: int | float | str)-> int | float | str | None:
    """

    Esta funcion elimina la primera ocurrencia de un elemento en una lista
    
    """
    indice = 0
    for i in lista:
        if i == elemento:
            elemento_eliminado = i
            lista[:] = lista[:indice] + lista[indice + 1:]
            return elemento_eliminado
        indice += 1
    
    return None
