def al_cuadrado(lista_de_numeros):
    """Funcion para realizar el cuadrado de una lista.
    Parametros:
    lista_de_numeros: numeros cualquiera en una lista.
    Salida:
    La lista introducida con los valores al cuadrado."""
    numeros_al_cuadrado = []
    for a in lista_de_numeros:
        numeros_al_cuadrado.append(a**2)
    return numeros_al_cuadrado
print (al_cuadrado([6,2,8,10]))
help(al_cuadrado)