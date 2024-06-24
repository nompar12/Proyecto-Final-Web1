#Las variables tn python son de tipado dinamico

name = "Alejandro"

#Notacion snake

last_name= " Villa Chica"
mail = " nompar89@gmail.com"
salary =9800000
state = True
note = 4.5
gener = " Men"

#print (mail)

#Hablemos de la contatenación

#print("Nombre: " + name +  last_name)

#Usando coma

#print("Nombre: " , name , last_name)

#Hablemos de contatenar usando format

print(f"Nombre:{name}\nApellidos:{last_name}\nCorreo:{mail}\nSalario:{salary}")

#Type que permite conocer de que tipo es una variable

print(type(salary))

#Como capturar datos desde la consola

phone = input("Telefono: ")

print(f"Telefono:{phone}")


aux_transporte = int(input("Ingrese el aux de transporte"))

total_salary = salary + aux_transporte

print(f"El salario total es:{total_salary}")
3244532707
per_loan_discount = 0.3

loan_discount = salary + aux_transporte - per_loan_discount

print(f"El salario total es:{total_salary}\n Descuentos: \n Prestamos: {loan_discount}")

