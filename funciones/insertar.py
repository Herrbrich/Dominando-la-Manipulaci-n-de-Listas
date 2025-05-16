def insertar(lista : list, elemento : str | int | float, indice : int )-> list:

    """
    La funcion agrega un elemento en la pocision seleccionada, si esta queda fuera de rango, la agrega al final.

    """

    if indice >= len(lista):
        lista += [elemento]
    else:
        lista[:] = lista[:indice] + [elemento] + lista[indice:]
    return lista