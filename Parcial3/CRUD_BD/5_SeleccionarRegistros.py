from ConexionBD import *
try:
    micursor=conexion.cursor()
    sql="SELECT * FROM clientes"
    micursor.execute(sql)
except:
    print("OCURRIO UN ERROR")
#Crear un objeto para enviar el resultado de la ejecucion del execute para posteriormente mostrar con un ciclo
resultado=micursor.fetchall()
for x in resultado:
    print(x)