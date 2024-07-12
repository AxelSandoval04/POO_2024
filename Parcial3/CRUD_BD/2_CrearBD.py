import mysql.connector
try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='axelitosipsip'
)   
except:
    print("OCURRIO UN ERROR CON EL SERVIDOR")   
else:
    
    #Crear un onjeto de tipo cursor que permita ejecutar instrucciones sql
    micursor=conexion.cursor()
    sql="CREATE database bd_Python"
    #Ejecutar la consulta
    micursor.execute(sql)
    
    if micursor:
        print("Se creo la BD exitosamente")
    #Mostrar las BD que existen en el SGDB MySQL
    micursor.execute("SHOW DATABASES")
    for x in micursor:
        print(x)