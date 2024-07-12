from ConexionBD import *
try:
    micursor=conexion.cursor()
    sql="update clientes set direcccion ='col Nueva' WHERE id=3"
    micursor.execute(sql)

    conexion.commit()
except:
    print("OCURRIO UN ERROR")
else:    
 print("Registro Actualizado correctamente")