"""
Existe una estructura de condicion la cual evalua una condicion para encontrar el valor TRUE o se cumple una condicion ejecuta la linea
o lineas de codigo
"""
# 1.- if simple 
# 2.- if compuesto
# 3.- if anidado
# 4.- if y elseif
# 1.+
color="rojo"
if color =="rojo":
    print("Soy el color rojo")
# 2-
if color =="rojo":
    print("Soy el color rojo")
else:
    print("No soy rojo")
# 3.-
if color =="rojo":
    print("Soy el color rojo")
    if color !="rojo":
      print("Soy otro rojo")
else: print("No soy rojo")
# 4.-
if color =="rojo":
    print("Soy el color rojo")
elif color =="negro":
    print("Soy el color Verde")
else:
    print("No soy ni Rojo ni Verde")

