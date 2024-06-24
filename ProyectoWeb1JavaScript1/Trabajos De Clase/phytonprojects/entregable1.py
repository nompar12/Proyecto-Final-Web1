
#Input

id = input("Ingrese el ID del producto: ")
nombre = input("Ingrese el nombre del producto: ")
descripcion = input("Ingrese la descripcion del producto: ")
costo = float(input("Ingrese el costo del producto: "))  
canti = int (input("Ingrese la cantidad del producto: "))
estado = input("Ingrese el estado del producto: ")

#Formulas

precio =  costo / (1 - 0.3)
precio1 = precio - costo 

#Print
print("ID:", id)
print("Nombre:", nombre)
print("Descripcion:", descripcion)
print("Precio:", precio)
print("Costo:", costo)
print("Cantidad:", canti)
print("Estado:", estado)
print("Porcentaje de ganancia:" , precio1)
