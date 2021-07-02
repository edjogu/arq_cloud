# 3. Crea un programa que se llame Promedio.py, que pida 5 números, y calcula el promedio.

# Usando funcion
def CheckPromedio (num1, num2, num3, num4, num5):
    total = (num1 + num2 + num3 + num4 + num5) / 5      
    return total

num1 = int(input("Escriba primer numero:" ))
num2 = int(input("Escriba segundo numero:" ))
num3 = int(input("Escriba tercer numero:" ))
num4 = int(input("Escriba cuarto numero:" ))
num5 = int(input("Escriba quinto numero:" ))

resultado = CheckPromedio(num1, num2, num3, num4, num5)
print(f"El promedio es: {resultado} ")

# Lineal
# num1 = int(input("Escriba primer numero:" ))
# num2 = int(input("Escriba segundo numero:" ))
# num3 = int(input("Escriba tercer numero:" ))
# num4 = int(input("Escriba cuarto numero:" ))
# num5 = int(input("Escriba quinto numero:" ))

# promedio = (num1 + num2 + num3 + num4 + num5) / 5
# print(f"El promedio es: {promedio}" ) 




