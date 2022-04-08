#Permitirle al usuario ingresar un diccionario de comidas donde las claves son el 
#nombre de las comidas y el valor el precio de estas. Las comidas se pueden ingresar 
#infinitamente hasta que el precio de una sea 0. Una vez finalizado el ingreso, debemos
#mostrarle al usuario las comidas con sus respectivos precios y permitirle elegir una y la 
#cantidad que va a comer. Si la comida que eligió el usuario no existe debemos mostrar 
#un error. Si la comida existe, mostrar el precio total que va a pagar.

menu = {}

comida = str(input("Ingrese nombre de la comida: "))
precio = int(input("Ingrese el valor de ese plato: "))

while precio > 0:

    if(precio > 0):
        menu[comida] = precio
        comida = str(input("Ingrese nombre de la comida: "))
        precio = int(input("Ingrese el valor de ese plato: "))
    
for platillo in menu.keys():
    print(f"{platillo} ......... $ {menu[platillo]}")

pedido = str(input("Que platillo va a pedir?: "))
cantidad = int(input("Que cantidad de platillos va a pedir?: "))

if pedido in menu.keys():
    print(f"Usted encargo {cantidad} {pedido} con un valor total de: $ {menu[pedido]*cantidad} ")
else:
    print("Error el platillo que ingreso no se encuentra en el menu")    