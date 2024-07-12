import mysql.connector


#conecar con la 80 en MySQL
try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='axelitosipsip',
        database='bd_python'
)
except Exception as e:
     print(f"Error:{e}")
     print(f"tipo de excepcion {type(e).__name__}")
     print("Ocurrio un error al conectarse con el servidor")
# except InterfaceError:
#    print("No es posible conectarse con el servidor")
   
else:
#verificar si la conexion
    if conexion.is_connected():
     print("Conectado correctamente")
    else:
     print("No fue posible conectarse con la BD")
