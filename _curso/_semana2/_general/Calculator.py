def menu():
    print("-------------------Titulo del Menu-------------------")
    print("1. Sumar")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciar")
    print("-----------------------------------------------------")

def calculadora(oper1, oper2, oper):
    if oper == 1:
        oper = "suma"
        return oper1 + oper2        
    elif oper == 2:
        return oper1 - oper2
    elif oper == 3:
        return oper1 * oper2
    elif oper == 4:
        return oper1 / oper2
    elif oper == 5:
        return oper1 ** oper2

#region Main
menu()
operador = int(input("Que operación desea realizar: "))
num1 = int(input("Escriba primer numero:" ))
num2 = int(input("Escriba segundo numero:" ))
resultado = calculadora(num1, num2, operador)
if operador == 1:
    oper = "suma"


print(f"El resultado de la operación {oper} es: {resultado}")

