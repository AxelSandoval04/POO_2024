from ConexionBD import *
try:
    micursor=conexion.cursor()
    sql="DELETE FROM clientes WHERE id=1"
    micursor.execute(sql)

    conexion.commit()
except:
    print("OCURRIO UN ERROR")
else:
    print("Registro Eliminado correctamente")
