""" 4.- Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
  y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

"""

lista = [1, 2, 3]
cadena = "Hola, mundo!"
entero = 42
logico = True

def tipo_de_dato(variable):
    if type(variable) == list:
        return "Es una lista."
    elif type(variable) == str:
        return "Es una cadena."
    elif type(variable) == int:
        return "Es un entero."
    elif type(variable) == bool:
        return "Es un booleano."
    else:
        return "Tipo de dato no reconocido."
def imprimir_mensaje_tipo(variable, numero):
    mensaje = tipo_de_dato(variable)
    print(f"Variable {numero}: {mensaje} Contenido: {variable}")
imprimir_mensaje_tipo(lista, 1)
imprimir_mensaje_tipo(cadena, 2)
imprimir_mensaje_tipo(entero, 3)
imprimir_mensaje_tipo(logico, 4)

