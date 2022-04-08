#Crear un programa que le permita al usuario ingresar 5 números validos (Un numero 
#valido es un número igual o mayor que 1) e imprimir cada vez que se ingresa un 
#numero si valido e invalido. Una vez finalizado el programa se debe imprimir la 
#cantidad de números inválidos ingresados.

cont = 0
contInvalidos = 0

while(cont <= 4):
    numero = int(input("Ingrese un numero mayor o igaul que uno: "))

    if (numero >= 1):
        print("El numero ingresado es correcto") 
        cont = cont + 1
    else:
        print("El numero que ingreso es invalido")
        contInvalidos = contInvalidos + 1
           

print(f"Usted ingreso un total de {contInvalidos} nros invalidos")