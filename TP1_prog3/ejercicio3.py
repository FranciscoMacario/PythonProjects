#Una profesora tiene un curso de 8 alumnos. Se deben poder cargar las notas de esos 8 
#alumnos y contar la cantidad de alumnos aprobados. Al finalizar se debe mostrar el 
#promedio de todo el curso.

cantAprob = 0
sumaNotas = 0

for i in range (0, 8):
    nota = int(input(f"Ingrese la nota del {i + 1}° alumno: "))

    if(nota >= 7):
        cantAprob = cantAprob + 1
        sumaNotas = sumaNotas + nota
    else:
        sumaNotas = sumaNotas + nota
          
promedio = sumaNotas/8
print(f"Cantidad de alumnos aprobados: {cantAprob}")
print(f"Promedio general: {promedio}")