quesos = ["Cheddar", "Edam", "Gouda"] # Lista original
numeros = [3, 2] # Lista original
# print(numeros) # Imprimo la lista numeros original
# # numeros[1] = 45  # Altero la list (contenido) en la posición [1]
# print(numeros) # Imprimo la lista numeros modificada 
# # vacia = []
# print(quesos[0]) # Imprimo la posicion [0] para mostrar el contenido 

# print("Salado" in quesos)
# print("Gouda" in quesos)

# # Recorrer una lista
# for queso in quesos:
#     print(queso)

# print(numeros) # Imprimo mi lista original
# for i in range(len(numeros)):
#     numeros[i] = numeros[i] * 2 # Altero el contenido de mi lista
#     print(numeros[i]) # Imprimo cada contenido modificado
# print(numeros) # Impimo la lista ya modificada

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)

# d = [0] * 4
# print(d)

# e = a * 3
# print(e)

# t = ["a", "b", "c", "d", "e", "f"]
# print(t[1:3])
# print(t[:4])
# print(t[3:])
# print(t[:])

# t[1:4] = ["x", "y"]
# print(t)
# t[1:4] = ["z", "w"]
# print(t)


# type([vacia])

# print(quesos, numeros, vacia)
# # Listas con varios tipos de datos
# lista1 = [1, "tres", True]

# # Listas anidadas
# lista2 = [1, [2, 3], 4]

# print(lista1, lista2)

# Usando la funcion list()
# lista3 = list()
# print (list(1, 2, 3))
# lista5 = list("Python")
# list = (1,2,3) 
# print(list)
# print(lista5)

# lista1 = list(1,2)
# print(lista1)

matriz= (  [[], 
            [], 
            []]
        )
print(matriz)

# a = array([[5.1, 7.4, 3.2, 9.9],
#            [1.9, 6.8, 4.1, 2.3],
#            [2.9, 6.4, 4.3, 1.4]])

# t = ["a", "b", "c"]
# t.append("d")
# print(t)

# t1 = ["a", "b", "c"]
# t2 = ["d", "e"]
# t1.extend(t2)
# print(t1)

# t3 = ["e", "c", "b", "a", "f", "e"]
# t3.sort()
# print(t3)

# t3 = t3.sort()
# print(t3)

# t4 = ["a", "b", "c"]
# # x = t4.pop(1)
# # print(t4)
# # print(x)

# # del t4[1]
# # print(t4)

# t4.remove("b")
# print(t4)

# t5 = ["a", "b", "c", "d", "e", "f"]
# del t5[1:5]
# print(t5)

# nums = [3, 41, 12, 9, 74, 15]
# print(len(nums)) # retorna longuitud
# print(max(nums)) # retorna Maximo
# print(min(nums)) # retorna Mínimo
# print(sum(nums)) # retorna Sumatoria
# print(sum(nums) // len(nums)) # Permite hacer operaciones, en este caso el promedio

# cadenas = ["Hola", "Saludo"]
# print(max(cadenas))
# print(len(cadenas))

# Promedio forma tradicional
# total = 0
# counter = 0
# while True:
#     inp = input("Escriba el numero: ")
#     if inp == "fin": break
#     valor = float(inp)
#     total = total + valor
#     counter += 1    

# promedio = float(total / counter)
# print(f"El promedio es: {promedio}")

# Promedio usando lista
numlista = list()
while True:
    inp = input("Escriba el numero: ")
    if inp == "fin": break

    valor = float(inp)
    numlista.append(valor)   

promedio = sum(numlista) / len(numlista)
print(f"El promedio es: {promedio}")



