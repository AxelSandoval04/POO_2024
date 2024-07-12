from ConexionBD import *
try:
    micursor=conexion.cursor()

    sql="CREATE TABLE clientes(id int primary key auto_increment,nombre varchar(60), direccion varchar(120), tel varchar(10))"

    micursor.execute(sql)
except:
    print("OCURRIO UN ERROR")
else:
    print("Se creó la tabla exitosamente")