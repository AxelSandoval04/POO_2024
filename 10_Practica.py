# Practica 10
# Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron
aprobados = 0
reprobados = 0
for i in range(1, 16):
    calif = int(input("Ingrese la calificacion del alumno: "))
    if calif <=60:
       reprobados += 1
    else:
        aprobados += 1
print("La cantidad de alumnos que aprobaron fue: ", aprobados)
print("La cantidad de alumnos que reprobaron fue: ", reprobados)       