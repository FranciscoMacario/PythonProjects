#Ingresar una cadena y devolver al usuario si la cadena está escrita en mayúsculas,
#minúsculas o una mezcla de ambas

cadena = str(input("Ingrese una cadena: "))
longitud = len(cadena)
mayus = 0
minus = 0
digit = 0
simbol = 0

for carac in cadena:
    if(carac.isupper()):
        mayus = mayus + 1 
    elif(carac.islower()):      
        minus = minus + 1 
    elif(carac.isdigit()):   
        digit = digit + 1
    else:
        simbol = simbol + 1
        
if(mayus == longitud):
    print("Su cadena esta escrita en Mayuscula")
elif(minus == longitud):
    print("Su cadena esta escrita en Minuscula")
else:
    longitud - mayus
    if(longitud > 0 and digit == 0 and simbol == 0):
        print("Su cadena es una mezcla de ambas")
    else:
        print("Su cadena contiene un digito o un simbolo vuelva a ingresarla solo con letras!")
            



