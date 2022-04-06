num = int(input("Ingrese un nro para ver sus tablas: "))
prod = 0
for x in range (0, 11):
    prod = num * x
    print(f"{num} x {x}: {prod}")

#Pedirle al usuario que ingrese un número y nosotros le tenemos que devolver hasta
#la tabla del 10 de ese número 