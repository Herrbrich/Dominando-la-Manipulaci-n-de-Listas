def eliminar(lista : list)->int | float | str :
    """
    esta funcion elimina el ultimo elemento de la lista y lo retorna
    ademas de modificar la lista original

    """
    ultimo_elemento = lista[-1]
    lista[:] = lista[:-1]
    return ultimo_elemento