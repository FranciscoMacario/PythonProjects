cad = str(input("Ingrese una cadena: "))
flag = 0
for carac in cad:
    if(carac.isupper()):
        print("Porfavor ingrese toda la cadena en minuscula ")
        flag = 1
        break

if(flag == 0):
    print("Su cadena esta bien escrita ")


#Ingresar una cadena y verificar si esta se encuentra escrita toda en minúscula, si es así
#devolver “Su cadena esta bien escrita”, sino, un mensaje que diga “Por favor ingrese toda
#la cadena en minúscula”
