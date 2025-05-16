def agregar_elemento(lista :list, elemento: int | float | str)-> list:
    """
    La funcion agrega un elemento al final de la lista y la retorna
    """
    lista += [elemento]
    return lista