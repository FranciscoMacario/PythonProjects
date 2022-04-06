edad = int(input("Ingrese su edad: "))
sueldo = int(input("Ingrese su sueldo: "))

if(sueldo >= 25000 and edad >= 20 or edad >= 30):
    print("debe pagar impuestos :(")
else:
    print("no debe pagar impuestos :D")

#Para pagar impuestos debemos:
#Cobrar mas de 25000 pesos y tener mas de 20 años O Tener mas de 30 años
#El usuario debe ingresar su sueldo y su edad y debemos contestarle si debe pagar o no impuestos.    