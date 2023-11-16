def factorial_n (numero):
    """Funcion para realizar el factorial de un numero entero positivo.
     
      Parametros: 
        - numero = Un numero entero positivo.
      Salida:
        - El factorial del numero entero.
    """
    if numero == 0:
        return 1
    else:
        return numero * factorial_n(numero-1)
numero = int (input ("Numero positivo:"))
print (f"el factorial del", numero, "es:", factorial_n(numero))