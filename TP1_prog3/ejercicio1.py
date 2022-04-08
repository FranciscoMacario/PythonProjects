#Para pagar impuestos el usuario debe:
#Cobrar más de 20000 pesos Y tener más de 18 años O Tener más de 30 años

edad = int(input("Ingrese su edad: "))
sueldo = int(input("Ingrese el sueldo que gana: "))

if(edad >= 18 and sueldo >= 20000 or edad >= 30):
	print("Debera pagar impuestos :(")
else:
	print("No debe pagar impuestos :D")	