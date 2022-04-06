pw = 1234
#hola esto es un comentario
num = 0000
while(num != pw):
    num = int(input("ingrese datos hasta coincidir con la contraseña de 4 caracteres: "))
    if(num != 1234):
        print("contraseña incorrecta ")
    else:
        print("Adivino la contraseña ") 

#Escribir un programa que almacene una contraseña en la variable pw y preguntarle
#al usuario que ingrese datos hasta que la contraseña sea correcta   