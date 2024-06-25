

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

    def getInfo(self):
        print(f"Marca: {self.getMarca} Color: {self.getColor}, Modelo: {self.getModelo} \n Velocidad: {self.getVelocidad} 
              Km/h y un potencia de {self.getCaballaje} hp")
        
print("objeto 1")
coche1=Coches()
print("objeto 2")
coche2=Coches()

    

#Para crear multiples objetos es necesario realizar multiples instancias de la misma clase
print("Objeto 3")
coche3=Coches()
coche3.setMarca=("Porsche")
coche2.setColor=("Amarillo")
coche3.setModelo=("2024")
coche3.setVelocidad=(320)
coche3.setCaballaje=(400)
