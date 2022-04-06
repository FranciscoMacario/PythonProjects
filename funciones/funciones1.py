#Crear un programa que permita ingresarle 2 números al usuario. Estos dos numeros se
#deben sumar, restar, multiplicar y dividir.
#Para esto se deben crear 4 funciones
#Cada función debe tener 2 parámetros y devolver un resultado para luego imprimirlo
#en pantalla


def suma(num1, num2):
    resultado = num1 + num2
    return resultado

def resta(num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicacion(num1, num2):
    resultado = num1 * num2
    return resultado

def division(num1, num2):
    resultado = num1 / num2
    return resultado

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

respuesta = suma(a, b)
print(f"{a} + {b}: {respuesta}")

respuesta = resta(a, b)
print(f"{a} - {b}: {respuesta}")

respuesta = multiplicacion(a, b)
print(f"{a} * {b}: {respuesta}")

respuesta = division(a, b)
print(f"{a} / {b}: {respuesta}")