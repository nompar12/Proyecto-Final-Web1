
users = []

user1 = [ 26,"Jose Gabriel", "Agudelo Vargas", 3135293973, "jgabrielagudelov@gmail.com", "H", 16, 2007]
user2 = [ 586,"Alejandro", "Gómez Sánchez", 3148634576, "alejito@email.com", "H", 17, 2006]
user3 = [ 98,"Sofia", "Zapata Mejía", 3124890778, "sofizooa@email.com", "M", 16, 2007]

users.append(user1)
users.append(user2)
users.append(user3)

print(users)


for item in users:
    print(item)

    print(users[1][3])
    
    
userIngreso = input("Ingrese el nombre de usuario")
claveIngreso = input("Ingrese la clave de usuario")

if userIngreso == user1[4] or user2[4] or user3[4] and claveIngreso == user1[7] or user2[7] or user3[7]:
  print ("Bienvenido")

else:
   
   print("error")