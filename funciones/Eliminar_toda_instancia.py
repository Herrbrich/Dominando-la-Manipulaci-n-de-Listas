def eliminar_todos(lista: list, elemento: int | float | str)-> list:
    
    indice = 0
    while indice < len(lista):
        if lista[indice] == elemento:
            lista[:] = lista[:indice] + lista[indice +1:]
        else:
            indice += 1
