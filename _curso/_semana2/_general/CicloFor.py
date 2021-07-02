# # Ciclo For
# palabra = "Python"
# for x in palabra:
#     print(x)

# for i in range(1, 10, 2):
#     print(i, end=", ")

# amigos = ["Joseph", "Glen", "Sally"]
# for amigo in amigos:
#     print("Feliz año nuevo:", amigo)
# print("¡Terminado!")

# mi_tupla = ("rosa", "verde", "celeste", "amarillo")
# for color in mi_tupla:
#     print(color)

# for year in range(2001, 2013):
#     print("Informes del año", str(year))

# mayor = None
# print("Antes: ", mayor)
# for valor in [3, 41, 12, 9, 74, 15]:
#     if mayor is None or valor > mayor:
#         mayor = valor
#     print("Bucle:", valor, mayor)
# print("Mayor: ", mayor)

# menor = None
# print("Antes: ", menor)
# for valor in [3, 41, 12, 9, 74, 15]:
#     if menor is None or valor < menor:
#         menor = valor
#     print("Bucle:", valor, menor)
# print("Menor: ", menor)

# Contadora
numeros_pares = 0
for i in range(0, 10):
    if i % 2 == 0: # indica número par
        numeros_pares += 1
print("Total de numeros pares encontrados: " + str(numeros_pares))

# Flag
notas = [5.65, 8.75, 6.23, 4.3, 10, 7.55]
hay_rajados = False # variable se inicializa en false
i = 0 # variable par controlar el ciclo while

while i < len(notas) and not hay_rajados:
    if notas[i] < 5:
        hay_rajados = True
    i += 1

if hay_rajados:
    print("Al menos hay un rajado")
else:
    print("Todos están aprobados")

# Acumuladora
sueldos = [1540.43, 3010.11, 980, 1200.8]
total = 0

for sueldo in sueldos:
    total += sueldo

salario_medio = total / len(sueldos)

print("Eltotal del dinerop ganado es de: " + str(total))
print("El salario medio es de: " + str(salario_medio))






