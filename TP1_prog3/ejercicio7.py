#Crear una función que reciba 2 listas precargadas por el usuario, donde se deben 
#eliminar los ítems de la lista 2 que coincidan con la lista 1 y retornar una nueva lista 
#con los ítems eliminados
#Permitirle cargar la lista_1 de al menos 5 items dentro
#Permitirle cargar la lista_2 de al menos 2 items dentro
#Las listas deben poder cargarse dinámicamente por el usuario, permitiéndole cambiar 
#los ítems cada vez que se ejecute el programa
#La función debe llamarse eliminar_lista

def eliminar_lista(lista1, lista2):
    for j in lista2:
        for i in lista1:
            if x == i:
             lista1.remove(j)
    return lista1        

lista1 = []
lista2 = []

print("Ingrese los numeros para la lista 1: ")
for x in range(0, 5):
    num = int(input(f"Ingrese el {x}° numero: "))
    lista1.append(num)

print("Ingrese los numeros para la lista 2: ")
for x in range(0, 2):
    num = int(input(f"Ingrese el {x}° numero: "))
    lista2.append(num)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 1 sin los elementos de la lista 2: {eliminar_lista(lista1, lista2)}")
