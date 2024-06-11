
total_calificaciones = 0
suma_calificaciones = 0
continuar = True
while continuar:
    nombre = input("Ingrese el nombre del estudiante: ")
    carrera = input("Ingrese la carrera del estudiante: ")
    calificacion1 = float(input("Ingrese la calificación 1 de la carrera: "))
    calificacion2 = float(input("Ingrese la calificación 2 de la carrera: "))
    calificacion3 = float(input("Ingrese la calificación 3 de la carrera: "))
    calificacion_final = float(input("Ingrese la calificación del proyecto final: "))
    
    promedio = (calificacion1 + calificacion2 + calificacion3) / 3
    promedio_final = (promedio + calificacion_final) / 2
    suma_calificaciones += promedio_final
    total_calificaciones += 1
    
    print("Nombre del estudiante:", nombre)
    print("La carrera del alumno es:", carrera)
    print("El promedio de los parciales del estudiante es:", promedio)
    print("El promedio final del estudiante es:", promedio_final)
    if promedio_final < 80:
        if calificacion_final > 50:
            print("Presenta extraordinario")
    respuesta = input("¿Desea ingresar los datos de otro estudiante? (Si/No): ")
    if respuesta != "si":
        continuar = False

if total_calificaciones > 0:
    promedio_general = suma_calificaciones / total_calificaciones
    print("El promedio de la calificación final de todos los alumnos es:", promedio_general)



