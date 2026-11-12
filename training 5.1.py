#training 5.1
#calcular 2 valores
def calcula_precio(a, b):
    return a + b
#le damos valores a la funcion
total = calcula_precio(10, 20) 
#le decimos que nos muestre el resultado 
print("El precio total es:", total) 

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
        tipo = input("tipo de cliente:")
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
