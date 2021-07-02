# MinTIC Reto 1 - Primera parte
# Autor: guzmanE
# Date        Description
# 23.06.21    Initial version
# --          --

# Sistema Login @ TicNet Corp @

# Define Variables
#
#region Variables

msgBienvenido = "Bienvenido al sistema de ubicación para zonas públicas WIFI"
msgError = "Error"
msgOk = "Sesión iniciada"
name = 52208
passw = 80225
captcha = 208
#endregion Variables

# RF01:
print(msgBienvenido)

# RF02:
userName = int(input("Nombre de usuario: "))

if name == userName:
    userPass = int(input("Contraseña: "))
    if passw == userPass:
        # RF03:
        # RF04:
        calDigito = ((8 // 2) + 8)  - (2 ** 2 + (5 * 2) - 2)
        valorCaptcha = int(input(f"Valor Captcha 208 + {calDigito}: "))
        if captcha == valorCaptcha:
            print(msgOk)
        else:
            print(msgError) 
    else:
        print(msgError) 
else:
    print(msgError)