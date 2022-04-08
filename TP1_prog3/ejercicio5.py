#A partir de la lista:
#numeros = [3, 8, 21, 17, 12, 20, 86, 71, 39]
#Crear una lista llamada numeros_pares que contenga todos los números pares y una 
#lista numeros_impares que contenga los números impares, una vez finalizado el 
#programa debemos mostrarle al usuario la cantidad de números en ambas listas.

numeros = [3, 8, 21, 17, 12, 20, 86, 71, 39]

numerosPares = []
numerosImpares = []

for x in range(0, len(numeros)):
    aux = numeros[x]
    if(aux % 2 == 0):
        numerosPares.append(aux)
    else:
        numerosImpares.append(aux)

print(f"En la lista numeros pares hay: {len(numerosPares)}")
print(f"En la lista numeros impares hay: {len(numerosImpares)}")