contDesaprobados = 0
contAprobados = 0

for x in range(0, 10):
    alum = int(input("Ingrese la nota del alumno: "))

    if(alum >= 7):
        contAprobados = contAprobados + 1
    else:
        contDesaprobados = contDesaprobados + 1

print(f"Aprobados: {contAprobados} Desaprobados: {contDesaprobados}")

#Una profesora tiene un curso de 10 alumnos y quiere ingresar las notas de todo el curso
#Se debe contar cuantos alumnos aprobaron (mayor o igual que 7)
#Y cuántos alumnos desaprobaron (menor que 7)        