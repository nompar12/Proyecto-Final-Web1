

datos_usuario = [1, "pepito", "apellido", "pepito@email.com", 1350000, True, 4.5, 1234]

print(datos_usuario.count(1)) # Cuenta los elementos repetidos en la lista
copia = datos_usuario.copy() #hace una copia de la lista

print(copia)

print(datos_usuario.index(1350000))




for dato in datos_usuario:
    print(dato)


datos_usuario.append("3214567890")

for dato in datos_usuario:
        print(dato)

datos_usuario.insert(2, "Albert")

for dato in datos_usuario:
        print(dato)


datos_usuario.pop(2)
datos_usuario.remove(4.5)

for dato in datos_usuario:
 print(dato)



numbers = []

numbers.append(5)
numbers.append(2)
numbers.append(1)
numbers.append(4)
numbers.append(3)

for number in numbers:
     print(number)

numbers.sort()

for number in numbers:
     print(number)

numbers2 =[6,7,8,9,10]
numbers.extend(numbers2)

for number in numbers:
     print(number)


numbers.clear()

for number in numbers:
     print(number)