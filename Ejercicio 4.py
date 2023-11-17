numeros = [10, 5, 8.84, 4]
def Media_numeros (numeros):
    """Funcion para realizar la media de una lista de numeros.
     Parametros:
      numeros: Es una lista de numeros.
      Formula: suma de la lista entre cada uno de los elementos de la lista
     Salida:
      La media de la lista de numeros """
    media = sum(numeros)/len(numeros)
    return media
print (Media_numeros(numeros))
help(Media_numeros)