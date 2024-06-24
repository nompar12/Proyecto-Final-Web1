user = "pp@mail.com"
key = 1234
phone: "5734567"

usuario_telefono = input("Que desea ingresar: ")
ingreso = input("")

clave = int(input("Ingrese la clave: "))
telefono = (input("Ingrese el telefono: "))


#Usando if else cree un sistema de login que valide las credenciales, si cumple permita iniciar sesion, si no vuelve a la pagina


if usuario_telefono == user and clave == 1234 and telefono == phone:
    print("Eres bienvenido")

else:
    print("Válide sus credenciales")