# Crear una lista y almacenar 10 enteros pedidos por teclado. Eliminar todos los elementos que sean iguales al número entero 5.

# listaenteros = list()
# counter = 0
# while counter < 10:
#     numero = input("Escriba el numero para agregar a la lista: ")
#     listaenteros.append(numero)   
#     counter += 1  
  
# print(listaenteros)


# Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores
listaenteros = list()
counter = 1
while counter <= 5:
    numero = int(input(f"Escriba el numero {counter} para agregar a la lista: "))
    listaenteros.append(numero)   
    counter += 1 
  
print(listaenteros)

for i in listaenteros:
    if i == 10:
        listaenteros.remove(i)
        print("Removiendo...")
        print(listaenteros)
    else:
        print("No hubo coincidencia")
print(listaenteros)       


