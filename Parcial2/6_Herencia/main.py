from coches import *
#Crear un objetos o instanciar la clase

print("Objeto 1")
coche1=Coche("Blanco","VW","2020",220,150,5)
coche1.getInfo()


print("Objeto 2")
coche2=Coche("Azul","NISSAN","2020",180,150,5)
coche2.getInfo()

print("Objeto 3")
camion1=Camiones("Azul","NISSAN","2020",180,150,5,12,300)
camion1.getInfo()

print("Objeto 4")
camion2=Camiones("Azul","NISSAN","2020",180,150,14,5,300)
camion2.getInfo()

print("Objeto 5")
camioneta1=Camionetas("Azul","NISSAN","2020",180,150,5,"Trasera",True)
camioneta1.getInfo()
print("Objeto 6")
camioneta2=Camionetas("Azul","NISSAN","2020",180,150,5,"Trasera",True)
camioneta2.getInfo()

print(coche1.publico_atributo)
#print(coche1.__privado) #Esto no es permitido


# print(coche1.getPrivadoAtributo())

