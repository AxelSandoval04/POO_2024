""""
 Crear los metodos setters y getters estos metodos son importantes y necesarios en todas las clases para que el programador
 interactue con los valores de los atributos a traves de estos metodos digamos que es la manera mas adecuada y recomendada para 
 solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributoen particular de la clase o a traves de un objeto
 En teoria se deberia de crear una metodo Getter y Setter por cada atributo que contenga la clase
 Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion.

"""
# Ejemplo 1 crear una clase (un molde para crear mas objetos ) llamada coches y aparte de la clase crear objetos o instancias (coche )
# con caracteristicas
#
class Coches:
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color=color

    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca

    def getModelo(self):
        return self.modelo
    def setModelo(self,modelo):
        self.modelo=modelo
    
    def getVelocidad(self):
        return self.velocidad
    def setVelocidad(self,velocidad):
        self.velocidad=velocidad
    
    def getCaballaje(self):
        return self.caballaje
    def setCaballaje(self,caballaje):
        self.caballaje=caballaje








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
print(f"Marca: {coche2.marca} {coche2.color}, numeros de plazas: {coche2.plazas} \nModelo: {coche2.modelo} con una velocidad de {coche2.velocidad} Km/h y un potencia de {coche2.caballaje} hp")

#Acelerar la velocidad del coche de 300 a 301
coche1.acelerar()
print(f"La nueva velocidad es: {coche1.velocidad}")
#Disminuir la velocidad del coche de 301 a 100

for i in range(1,202):
   coche1.frenar()

print(f"La nueva velocidad del coche es: {coche1.velocidad}")