""""
 Programacion Orientada a Objetos POO o OOP
 CLASES.-.- es como un molde a traves del cual se pueden instanciar un objeto dentro de las clases 
 se definen atributos (propiedades / caracteristicas ) y los metodos (funciones o acciones)

 Objetos o Instancias.-.- soon parte de una clases los objetos o instancias pertenecen a una clase es decir para 
 interactuar con la clase o clase y hacer uso de los atributos y metodos es necesario crear un pbjeto o objetos.

"""
# Ejemplo 1 crear una clase (un molde para crear mas objetos ) llamada coches y aparte de la clase crear objetos o instancias (coche )
# con caracteristicas
#
class Coches:
    #Atributos
    marca="Ferrari"
    color="rojo"
    modelo="2010"
    velocidad=300
    caballaje=500
    plazas=2
    #Metodos
    def acelerar(self):
        self.velocidad+=1
    def frenar(self):
        self.velocidad+=1
#Definir clase

#Crear un objeto o instancia
coche1=Coches()
# Mostrar los valorres iniciales del objetos
print(f"Marca: {coche1.marca} {coche1.color}, numeros de plazas: {coche1.plazas} \nModelo: {coche1.modelo} con una velocidad de {coche1.velocidad} Km/h y un potencia de {coche1.caballaje} hp")

coche2=Coches()
coche2.marca="Porsche"
coche2.color="Amarillo"
coche2.modelo="2020"
coche2.velocidad=320
coche2.caballaje=600
coche2.plazas=4
print(f"Marca: {coche2.marca} {coche2.color}, numeros de plazas: {coche2.plazas} \nModelo: {coche2.modelo} con una velocidad de 
      {coche2.velocidad} Km/h y un potencia de {coche2.caballaje} hp")

#Acelerar la velocidad del coche de 300 a 301
coche1.acelerar()
print(f"La nueva velocidad es: {coche1.velocidad}")
#Disminuir la velocidad del coche de 301 a 100

for i in range(1,202):
   coche1.frenar()

print(f"La nueva velocidad del coche es: {coche1.velocidad}")