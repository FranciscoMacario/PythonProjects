def tabla(num1):
    for x in range(0, 11):
        result = num1 * x
        print(f"{num1} * {x} : {result}")

num1 = int(input("ingrese un nuemro: "))

tabla(num1)

#Crear un programa que le permita al usuario ingresar un numero y que le devuelva
#la tabla del 10 de ese numero. Para esto se debe usar la función –tabla