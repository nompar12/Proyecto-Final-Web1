usuario = {}

id_user = int (input("Ingrese el id"))
usuario.update({"id": id_user})
name_user = input ("Nombre")
usuario.update ({"Nombre": name_user})
email_user = input
usuario.update ({"mail": email_user})
clave = input ("Clave")
usuario.update ({"Clave": clave})

print (usuario)

usuario.popitem ()
print(usuario)