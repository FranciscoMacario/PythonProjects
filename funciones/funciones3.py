def espar(num1):
    if(num1 % 2 == 0):
        return 1
    else:
        return 0

num1 = int(input("ingrese un numero: "))

if(espar(num1)):
    print("Es par")
else:
    print("Es impar")

# Crear la función –es_par que tenga como parámetro un numero, y dependiendo de
#este devolver 1 si es par y 0 si impar    