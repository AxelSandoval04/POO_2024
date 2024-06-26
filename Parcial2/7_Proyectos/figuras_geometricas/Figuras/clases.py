class Figura:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visible = True
    def estaVisible(self):
        return self.visible
    def calcular_area(self):
        pass
    def ocultar(self):
        self.visible = False

    def mostrar(self):
        self.visible = True

class Rectangulo(Figura):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def mostrar():
        print(Rectangulo)
    
    @property
    def Largo(self):
        return self.largo

    @Largo.setter
    def Largo(self, valor):
        self.largo = valor

    @property
    def Ancho(self):
        return self.ancho

    @Ancho.setter
    def Ancho(self, valor):
        self.ancho = valor

    def calcular_area(self):
        return self.largo * self.ancho

class Circulo(Figura):
    def __init__(self, radio):
        self.radio=radio
    

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura

