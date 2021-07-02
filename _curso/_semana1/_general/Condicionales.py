# Estructuras Condicionales
# Operadores Relacionales
# Operadores Lógicos (para evaluar más de una condición)
# If Elif Else

# x = 10
# if x%2 == 0:
#     print(x, "Es par")    
# else:
#     print(x, "No Es par") 

# valores = [1, 3, 4, 8]
# if 5 in valores:
#     print('está en valores')
# print('fin')

# If Elif Else
# x = 10
# y = 10
# if x < y:
#     print(x, 'es menor que', y)
# elif x > y:
#     print(x, 'es mayor que', y)
# else:
#     print(x, 'y', y, 'son iguales')

# Operadores Lógicos
# x = 3
# if 0 < x:
#     if x < 10:
#         print(x, 'es un numero positivo con un solo digito.')

# y = 3
# if 0 < y and y < 10:
#     print(y, 'es un numero positivo con un solo digito.')

# compra = 250
# if compra <= 100:
#     print("Pago en efectivo")
# elif compra > 100 and compra < 300:
#     print("Pago con tarjeta de debito")
# else:
#     print("Pago con tarjeta de crédito")

# importeAPagar = 0
# totalCompra = 200
# tasaDescuento = 0
# importeDescuento = 0
# if totalCompra > 100:
#     tasaDescuento = 10
#     importeDescuento = totalCompra * tasaDescuento/100
#     importeAPagar = totalCompra - importeDescuento
#     print("Su desceunto es: ", importeDescuento, "y su total a pagar es:", totalCompra)

# edad = int(input("Ingresa la edad actual: "))

# if edad <= 18:
#     print("es menor de edad")
# elif edad > 65:
#     print("es jubilado")
# else:
#     print("esta activo")
# Hora Actual
# horaActual = int(input("Ingresa la hora actual: "))
# if horaActual >= 1 and horaActual <=13:
#     print("Buenos días")
# elif horaActual > 13 and horaActual <= 18:
#     print("Buenas tardes")
# elif horaActual <= 24:
#     print("Buenas noches")
# else:
#     print("fuera de horario")

# escribir un programa que calcule una devuelta sobre una compra
# con un valor constante.

# valorCompra = 200
# #valorDevuelto = 0
# montoPago = 10000

valorCompra = int(input("Por favor, digite el valor de la compra: $"))
montoPago = int(input("Por favor, valor del billete a pagar: $"))
if valorCompra >= montoPago:
    print("Falta dinero")
elif valorCompra < montoPago:
    print("Su cambio es: $", montoPago - valorCompra)
else:
    print("Problemas con la compra!")

















