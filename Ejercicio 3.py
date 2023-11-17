
def area_circulo (r):
    """Funcion para calcular el area del circulo.
     Parametros:
      r: El radio del circulo.
      Formula del circulo: π * radio al cuadrado.
     Salida:
     El area del circulo con el radio indicado."""
    import math
    a = (math.pi * (r)**2)
    return a
r = float (input ("Radio del circulo:"))
print (area_circulo (r))
def volumen_cilindro (r, h):
    """Funcion para calcular el volumen del cilindro.
     Parametros:
      r: Radio del circulo.
      h: Altura del cilindro.
      Formula del volumen del cilindro: area del circulo  * la altura del cilindro.
     Salida:
      El volumen del cilindro con el area del circulo y la altura del cilindro."""
    v = (area_circulo(r) * h)
    return v
h = float (input ("Altura del cilindro:"))
print (volumen_cilindro (r,h))
help(area_circulo)
help(volumen_cilindro)