print("Adrian Ozuna | #19 | 5toC")
print("Crear un programa que pida al usuario que se registre en un sistema")

usuario1 = ""
password1 = ""
usuario2 = ""
password2 =""
userLogin = ""
passwordLogin = ""
userRegister = ""
passwordRegister = ""
libreDeError = True

while True:
    accion = int(input("Que accion desea realizar?: Loguearse (1) | Registrarse (2): "))
    if(accion == 1 or accion == 2):
        break
    else:
        continue
while True:
    if(accion == 1):
        while True:
            print("Bienvenido al login.")
            userLogin = input("Ingrese el usuario: ")
            passwordLogin = input("Ingrese la contraseña: ")
            
            if(userLogin == usuario1 and passwordLogin == password1):
                print("Bienvenido ", usuario1)
                break
            elif(userLogin == usuario2 and passwordLogin == password2):
                print("Bienvenido", usuario2)
                break
            else:
                print("El usuario y/o la contraseña son incorrectos. Por favor intentelo nuevamente.")
                continue
    elif(accion == 2):
        while True:
            print("Bienvenido al registro.") 
            userRegister = input("Ingrese el usuario a registrar: ")
            if((userRegister == usuario1) or (userRegister == usuario2)):
                print("Este usuario ya existe")
                continue
            else:    
                usuario1 = userRegister
                
                while True:
                    passwordRegister = input("Ingrese la contraseña: ")
                    passwordConfirm = input("Vuelva a escribir la contraseña: ")
                
                    if(passwordRegister != passwordConfirm):
                        print("Las contraseñas no conciden. Vuelva a intenarlo.")
                        continue
                    else:
                        password1 = passwordRegister
                        print("Usario registrado correctamente.")
                        
                        while True:
                            eleccionRegistro = int(input("Desea registrar otro usuario?: Si (1) | No (2): "))
                            if(eleccionRegistro == 1): 
                                while True:
                                    userRegister = input("Ingrese el usuario a registrar: ")
                                    if(userRegister == usuario2):
                                        print("Este usuario ya existe")
                                        continue
                                    else:    
                                        usuario2 = userRegister
                                        while True:
                                            passwordRegister = input("Ingrese la contraseña: ")
                                            passwordConfirm = input("Vuelva a escribir la contraseña: ")
                                        
                                            if(passwordRegister != passwordConfirm):
                                                print("Las contraseñas no conciden. Vuelva a intenarlo.")
                                                continue
                                            else:
                                                password2 = passwordRegister
                                                print("Usario registrado correctamente.")
                                                break
                            elif(eleccionRegistro == 2):
                                print("gerg")
                                break
                            else:
                                print("La opcion que eligio es incorrecta. Vuelva a intentarlo.")
                                continue
                        break
                    break
                break
            break
        break
    else:
        print("La opcion que eligio es incorrecta. Vuelva a intentarlo.")
        continue
    
while True:
    print("Bienvenido al login.")
    userLogin = input("Ingrese el usuario: ")
    passwordLogin = input("Ingrese la contraseña: ")
    
    if(userLogin == usuario1 and passwordLogin == password1):
        print("Bienvenido ", usuario1)
        break
    elif(userLogin == usuario2 and passwordLogin == password2):
        print("Bienvenido", usuario2)
        break
    else:
        print("El usuario y/o la contraseña son incorrectos. Por favor intentelo nuevamente.")
        continue
