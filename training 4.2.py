#iniciamos una variable
hay_diez = False

#pedimos la primera nota 
nota = int(input("Introduce la nota (-1 para terminar)"))

#repetimos minetras la nota sea -1 
while nota != -1:

    #comprobamos si la nota es mayor o igual a 10
    if nota == 10:
        hay_diez = True

    #pedimos la siguiente nota
    nota = int(input("Introduce la nota (-1 para terminar)"))

#cuando termine bucle mostramos el resultado
if hay_diez:
    print("Hi ha alguna nota que te un 10")
else:
    print("No hi ha cap nota que te un 10")
