#los errores de exxcepciones en un lenguaje de programacion no es otra cosa que los errores en tiempo de ejecucion
#n tiempo de ejecucion.... cuando se manejan los errores mediante las excepciones en realidad se dice que se evita que se presenten
#esos errores en programa en timepo ejecucion

#ejemplo cuando s epresenta un error cuando no es generada una variable.
try:
 nombre=input("dame el nombre de una persona: ")
 if len(nombre)>0:
    nombre_usuario="El nombre del usuario del sistema es: ",nombre
 print(nombre_usuario)
except:
 print("No ingresaste ningun caracter")

#ejemplo 2 cuando se solicita un numero y se ingresa otra cosa

try:
  numero=int(input("Ingrese un numero"))

  if numero>0:
    print("Soy un numero positivo")
  else:
    print("Soy un numero negativo")
except ValueError:
    print("Favor de solo introducir valores numericos")

#ejemplo cuando se generan multiples excepciones
try:
  
    numero=int(input("Ingrese un numero: "))
    print("el cuadrado del numero es:",str(numero*numero))

except TypeError:
  print("No coinciden los tipos de datos")
except ValueError:
  print("Debes introducir un numero")
else:
  print("Todo se ejecutó sin errores")