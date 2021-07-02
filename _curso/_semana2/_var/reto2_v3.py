# MinTIC Reto 2 - Primera parte
# Autor: guzmanE
# Date        Description
# 01.07.21    Initial version
# --          --

# Sistema Login @ TicNet Corp @

# Define Variables
#

import time
import os

#region Variables Globales

msgBienvenido = "Bienvenido al sistema de ubicación para zonas públicas WIFI"
msgError = "Error"
msgOk = "Sesión iniciada"
name = 12345 #52208
passw = 123 #80225
captcha = 208
iMenu01 = "Cambiar contraseña";
iMenu02 = "Ingresar coordenadas actuales";
iMenu03 = "Ubicar zona wifi más cercana";
iMenu04 = "Guardar archivo con ubicación cercana";
iMenu05 = "Actualizar registros de zonas wifi desde archivo";
iMenu06 = "Elegir opción de menú favorita";
iMenu07 = "Cerrar sesión";
# Definir lista 
optMenuList = [iMenu01, iMenu02, iMenu03, iMenu04, iMenu05, iMenu06, iMenu07];
countErrors = 0

#endregion Variables Globales

# RF01:
print(msgBienvenido)

userName = int(input("Nombre de usuario: "))

if name == userName:
    userPass = int(input("Contraseña: "))
    if passw == userPass:
        calDigito = ((8 // 2) + 8)  - (2 ** 2 + (5 * 2) - 2)
        valorCaptcha = int(input(f"Valor Captcha: {captcha} + {calDigito}: "))
        if captcha == valorCaptcha:
            os.system("cls")
            print(msgOk)
            time.sleep(2)
            while countErrors < 3:
                # RF01
                for y in range(len(optMenuList)):
                    print(f"{y + 1} - {optMenuList[y]}")            
                #region RF03
                selectOpt = int(input("Elija una opción: "))
                if selectOpt > 0 and selectOpt < 8:
                    selectOptList = optMenuList[selectOpt-1]
                    if selectOptList == iMenu01:
                        print(f"Usted ha elegido la opción: {selectOpt}")
                        time.sleep(2)
                    elif selectOptList == iMenu02:
                        print(f"Usted ha elegido la opción: {selectOpt}")
                        time.sleep(2)
                    elif selectOptList == iMenu03:
                        print(f"Usted ha elegido la opción: {selectOpt}")
                        time.sleep(2)
                    elif selectOptList == iMenu04:
                        print(f"Usted ha elegido la opción: {selectOpt}")
                        time.sleep(2)
                    elif selectOptList == iMenu05:
                        print(f"Usted ha elegido la opción: {selectOpt}")
                        time.sleep(2)
                    elif selectOptList == iMenu06:
                        #region RF02
                        newFavOpt = int(input("Seleccione opción favorita: "))
                        if newFavOpt == 1 or newFavOpt == 2 or newFavOpt == 3 or newFavOpt == 4 or newFavOpt == 5:
                            # Doble check for user
                            check1 = int(input("Para confirmar por favor responda: Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es: "))
                            if check1 == 0:
                                check2 = int(input("Para confirmar por favor responda: Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es: "))
                                if check2 == 8:
                                    tempOpt = optMenuList[newFavOpt-1]
                                    optMenuList.remove(tempOpt)
                                    optMenuList.insert(0, tempOpt)                                    
                                else:
                                    os.system("cls")
                                    print(msgError)
                                    time.sleep(2)
                            else:
                                os.system("cls")
                                print(msgError)
                                time.sleep(2)
                        else:
                            os.system("cls")
                            print(msgError)
                            time.sleep(2)
                            continue #Regresa al inicio del bucle  
                        #endregion RF02                      
                    #region RF05
                    elif selectOptList == iMenu07:
                        os.system("cls")
                        print("Hasta pronto")
                        time.sleep(2)
                        exit()
                    #endregion RF05
                else:
                    countErrors += 1 # Incremento el contador
                    os.system("cls")
                    print(msgError)
                    time.sleep(2)
                    continue
                #endregion RF03
        else:
            print(msgError) 
    else:
        print(msgError) 
else:
    print(msgError)