from clases import Rectangulo, Circulo, Triangulo

rectangulo1 = Rectangulo(largo=5, ancho=3, x=10, y=20)    
rectangulo2 = Rectangulo(largo=7, ancho=4, x=15, y=25)
circulo1 = Circulo(radio=2, x=30, y=40)
circulo2 = Circulo(radio=2, x=30, y=40)

print("Área del Rectángulo:", rectangulo1.calcular_area())
print(rectangulo1.estaVisible())
print("Área del Rectángulo:", rectangulo2.calcular_area())
print("Área del Círculo:", circulo1.calcular_area())
print(circulo1.estaVisible())
print("Área del Círculo:", circulo2.calcular_area())

