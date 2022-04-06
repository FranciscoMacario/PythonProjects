num1 = int(input("Ingrese un numero: "))
div = int(input("Ingrese un divisor: "))

if(div == 0):
    print("Error")
else:
    division = num1/div
    print(f"{num1}/{div}:{division} ")

#Pedirle al usuario que ingrese dos números, si el divisor es 0 mostrar en la pantalla
#un mensaje que diga “Error”, si el divisor es diferente de 0 mostrar el resultado de esa
#división.    