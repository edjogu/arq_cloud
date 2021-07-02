# If anidados
# dia = "Viernes"

# if dia == "Lunes":
#     print(f"{dia} Primer día de la semana")
# elif dia == "Martes":
#     print(f"{dia} Segundo día de la semana")
# elif dia == "Miercoles":
#     print(f"{dia} Tercer día de la semana")
# elif dia == "Jueves":
#     print(f"{dia} Cuarto día de la semana")
# elif dia == "Viernes":
#     print(f"{dia} Quinto día de la semana")
# else:
#     print(f"{dia} Día no encontrado")

# Switch
# Uso de Switch
# def switch_demo(mes):
#     switcher = {
#         1: "Enero",
#         2: "Febrero",
#         3: "Marzo",
#         4: "Abril",
#         5: "Mayo",
#         6: "Junio",
#         7: "Julio",
#         8: "Agosto",
#         9: "Septiembre",
#         10: "Octubre",
#         11: "Noviembre",
#         12: "Dicimembre",
#     }
#     print (switcher.get(mes, "Mes invalido"))

# switch_demo(13)

# region Define funciones
#
#  Funcion menu
def menu():
    print("-------------------Titulo del Menu-------------------")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("-----------------------------------------------------")

# Funcion default
def default():
    return "Opción no válida"

# Funcion switch
def switch(case, a, b):
    switcher = {
        1: (a,b),
        2: (a,b),
        3: (a,b),
        4: (a,b),
    }
    return switcher.get(case, default())

#endregion funciones
a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
menu()
case = int(input("Selleccione una opción: "))
j = switch(case,a,b)
print(j)


