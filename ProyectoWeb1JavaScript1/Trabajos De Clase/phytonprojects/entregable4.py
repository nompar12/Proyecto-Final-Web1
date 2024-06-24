producto = []

producto1 = [1, "Milo", "8000", 580, "Milo"]
producto2 = [2, "Chocolisto", "12500", 315, "Chocolisto"]
producto3 = [3, "Nesquik", "6000", 250, "Nesquik"]
producto4 = [4, "Chocolate", "15300", 180, "Chocolate"]
producto5 = [5, "Nescafé", "18900", 200, "Nescafé"]

producto.append(producto1)
producto.append(producto2)
producto.append(producto3)
producto.append(producto4)
producto.append(producto5)

campos = 5

i = 0

while i < campos:
    valor = input("Ingrese campo")
    producto.append(valor)
    i+=1


encabezados = ("Id", "Nombre", "Precio", "Cantidad", "Categoria")

for encabezado in encabezados:
        print(encabezado, end="\t")
print()
for item in producto:
    print(item, end="\t")