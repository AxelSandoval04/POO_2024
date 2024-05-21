# Practica 8
# Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?

numero = float(input("Ingrese el número: "))
porcentaje = float(input("Ingrese el porcentaje (en porcentaje): "))

resultado = (porcentaje / 100) * numero
print(f"EL {porcentaje} % de {numero} es {resultado}")
