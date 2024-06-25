"""
Programación Orientada a Objetos (POO) o OOP

Clases: es como un molde a través del cual se puede instanciar un objeto. Dentro de las clases se 
definen atributos (propiedades/características) y los métodos (funciones o acciones).

Objetos o instancias: son parte de una clase, los objetos o instancias pertenecen a una clase.
Es decir, interactúan con la clase o clases y para hacer uso de los atributos y métodos es necesario
crear un objeto u objetos.

Método constructor: este método especial se coloca dentro de la clase y se utiliza para dar un valor a
los atributos del objeto de crear
"""

"""
Ejemplo 1: crear una clase (un molde para crear más objetos) llamada Coche y a partir de la clase
crear objetos o instancias (coche) con características similares.
"""

class Coche:
    """
    - Atributos o propiedades (variables)
    - Características del coche
    - Valores iniciales es posible declarar al principio de una clase
    """

    def _init_(self, marca, color, modelo, velocidad, caballaje, plazas):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    #def _init_(self, marca, color):
        #self.marca = marca
        #self.color = color  

    # Métodos o acciones o funciones que hace el objeto

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getColor(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    def getMarca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def getModelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def getVelocidad(self):
        return self.velocidad

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def getCaballaje(self):
        return self.caballaje

    def set_caballaje(self, caballaje):
        self.caballaje = caballaje

    def getPlazas(self):
        return self.plazas

    def set_plazas(self, plazas):
        self.plazas = plazas

    def getInfo(self):
        print( f"Marca: {self.getMarca}, Color: {self.getColor}, 
        Modelo: {self.getModelo}, Velocidad: {self.getVelocidad}, 
        Caballaje: {self.getCaballaje}, Plazas: {self.getPlazas}")
    """""
        En python el encapsulamiento tambien se le llama visibilidad y por lo general define como seran
        los atributos y metodos es decir publicos o privados
    """
    #Atributo publico
    publico_atributo="Soy un atributo publico"
    #Atributo privado
    __privado_atributo="Soy un atributo privado"

    #Nota 1: para utilizar un atributo privado, se tendría que hacer dentro de un método que fuera publico
    def getPrivadoAtributo(self):
        return self.__privado_atributo
    
    #Metodo privado
    def __getFuncionPrivada(self):
        print("Soy un metodo privado")

    #por medio del doble __ python identifica que el atributo o el metodo es privado

class Camiones(Coche):
    def _init_(self, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        super()._init_(marca, color, modelo, velocidad, caballaje, plazas)
        self.__eje=eje
        self.__capacidadCarga=capacidadCarga

    __tipo_carga=""
    def cargar(self,tipo_carga):
        self.__tipo_carga=tipo_carga
        return self.__tipo_carga        
    
    def getEje(self):
        return self.__eje
    
    def setEje(self,eje):
        self.__eje=eje

    def getCapacidadCarga(self):
        return self.__capacidadCarga
    
    def setCapacidadCarga(self,capacidadCarga):
        self.__capacidadCarga=capacidadCarga

    def getInfo(self):
        print( f"Marca: {self.getMarca}, Color: {self.getColor}, 
        Modelo: {self.getModelo}, Velocidad: {self.getVelocidad}, 
        Caballaje: {self.getCaballaje}, Plazas: {self.getPlazas} 
        Eje: {self.getEje} Cerrada: {self.getCapacidadCarga}")
    
class Camionetas(Coche):
    def _init_(self, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        super()._init_(marca, color, modelo, velocidad, caballaje, plazas)
        self.traccion=traccion
        self.cerrada=cerrada

    num_pasajeros=0
    def transportar(self,num_pasajeros):
        self.num_pasajeros=num_pasajeros
        return self.num_pasajeros
    
    def getTraccion(self):
        return self.traccion
    
    def setEje(self,traccion):
        self.traccion=traccion

    def getCapacidadCarga(self):
        return self.cerrada
    
    def setCapacidadCarga(self,cerrada):
        self.cerrada=cerrada
    
    def getInfo(self):
        print(f"Marca: {self.getMarca}, Color: {self.getColor}, 
        Modelo: {self.getModelo}, Velocidad: {self.getVelocidad}, 
        Caballaje: {self.getCaballaje}, Plazas: {self.getPlazas} 
        Traccion: {self.getTraccion} Cerrada: {self.getCapacidadCarga}")
    

