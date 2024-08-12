#Sergio Alexander Melendez Rodriguez
lista1 = (6, 4, 2, 34, 22, 77, 2, 9, 10, 11)
cantidad = (0)

def puntonum1 (lista1):

    for i in range (len(lista1)):
        cantidad = lista1.count(lista1, 0, len(lista1))
        cantidad.append [i]
        i += 1

    if cantidad > (len(lista1)) == True:
        print ("hay numeros repetidos en lista1")
    else:
        print ("no hay numeros repetidos en lista1")


