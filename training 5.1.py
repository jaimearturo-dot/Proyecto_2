#training 5.1
#calcular 2 valores
def calcula_precio(a, b):
    return a + b
#le damos valores a la funcion
total = calcula_precio(10, 20) 
#le decimos que nos muestre el resultado 
print("El precio total es:", total) 
#========================================
#Ejercicio 5
#1 -¿Cuantos parametros tiene la funcion? R - Hay 2 parametros los cuales son a y b
#2 -¿Que valor vuelve? R - La funcion devuelve la suma de los dos parametros que se le pasan
#3 -¿Que pasa si eliminas el return? R - Al ser eliminado, no podremos saber cumplir con la accion de la funcion solicitada.

#Training 5.2
#calcular descuentos dependinedo del precio
def calcula_descuento(precio, tipo_cliente):
    #hacemos una condicion para saber que tipo de client is
    decuento = 0
    if tipo_cliente == "particular":
        descuento = precio * 0.05
    elif tipo_cliente == "empresa":
        descuento = precio * 0.10
    elif tipo_cliente == "habitual":
        descuento = precio * 0.15
    else:
        print("Tipo de cliente no válido")
    precio_final = precio - descuento
    return precio_final
#le decimos que imprima el resultado de la funcion
precio_final = calcula_descuento(100, "particular")
precio_final2 = calcula_descuento(100, "empresa")
precio_final3 = calcula_descuento(100, "habitual")
print("El precio final para un cliente particular es:", precio_final)
print("El precio final para un cliente empresa es:", precio_final2) 
print("El precio final para un cliente habitual es:", precio_final3)

#Training 5.3
#calcular el IVA y la facturacion
def calcula_iva(precio):
    iva = precio * 0.21 #proporcionamos el descuento de este valor
    return iva
#hacemos que la funcion de facturacion llame a las otras dos funciones para calcular el precio final y el iva
def calcula_facturacion(precio, tipo_cliente):
    precio_descuento = calcula_descuento(precio, tipo_cliente)
    iva = calcula_iva(precio_descuento)
    facturacion = precio_descuento + iva
    return facturacion
#imprimimos el resultado de la funcion de facturacion para cada tipo de cliente
print(calcula_facturacion(100, "particular"))
print(calcula_facturacion(100, "empresa"))
print(calcula_facturacion(100, "habitual"))

#Training 5.4
#Creacion un menú para gestionar reparaciones de un "servicio técnico"
reparaciones = 0
facturacion = 0
opcion = 0
#creacion de menu 
def mostrar_menu():
    print("1. nueva reparación")
    print("2. consultar reparaciones")
    print("3. consultar facturacion")
    print("4. Salir")
while opcion != 4:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        piezas = float(input("precios de las piezas: "))
        mano_obra = float(input("precio de la mano de obra: "))
        precio = calcula_precio(piezas, mano_obra)
        tipo = input("tipo de cliente (particular, empresa, habitual):")
        total = calcula_facturacion(precio, tipo)
        print("total de la facturacion, total, €:", total)
        reparaciones += 1
        facturacion = facturacion + total
    elif opcion == 2:
        print("reparaciones", reparaciones)
    elif opcion == 3:
        print("facturacion total, €:", facturacion)
    elif opcion == 4:
        print("hasta pronto")
    else:
        print("opcion incorrecta")
#========================================
#Ejercicio 5 Relflexion
#4 -¿Cual es la diferencia entre "print() y return? 
# R - "print()" se encarga de de "imprimir el mensaje y mostrarlo, "return" se encarga dar el resultados de 2 valores dependiendo de la operatcion que se mande a realizar.
#5 -¿por que es mejor dividir un programa en funciones?
# R - Por que una funcion es reutilizable y la podemos estar repitiendo varias veces en el mismo o en un diferente programa donde podremos adaptar esa funcion basandonos a nuestras necesidades.
#6 -¿Que es un parametro en python?
# R - Es un valor que nos ayuda a darle sentido a una estructura donde manejamos funciones y acciones, ya que actúa como un marcador de posición para los valores que la función espera recibir y este parametro son valores que van adentro de las "()" en las estructuras de programacion.
#7 -¿Que es una variable local?
# R - Es Es una variable que cuando se creada dentro de una función que solo existe y puede utilizarse dentro de ella, cuando se termina la función, esta variable desaparece de su 
#8 -¿que ventajas tiene el reutilizar una funcion?
#9 - Nos 1
# R -ahorra tiempo a la hora que tener que volver a utilizar este codigo y evitamos duplicar líneas de código (de forma inesesaria) y nos facilita el mantenimiento o gestion de codigo o estructura.