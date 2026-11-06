#inicializamos una variable 
hay_diez = False

#repetimos 10 veces
for i in range(10):
    numero = int(input("Introduce un numero: "))

    #comprobamos si es negativo
    if numero < 0:
        hay_negativo = True

#mostrando el resultado
if hay_negativo:
    print("Hi havia almenys un nombre negatiu") 
else:
    print("No hi ha cap nombre negatiu")
