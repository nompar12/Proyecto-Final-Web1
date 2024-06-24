clientes = {}
productos = {}
ventas = []

def registrar_cliente():
    id_cliente = int(input("Ingrese el ID del cliente: "))
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    email_cliente = input("Ingrese el correo electrónico del cliente: ")
    clave_cliente = input("Ingrese la clave del cliente: ")
    clientes[id_cliente] = {"nombre": nombre_cliente, "email": email_cliente, "clave": clave_cliente}

def ver_clientes():
    print("Listado de clientes:")
    for key, value in clientes.items():
        print(f"ID: {key}, Nombre: {value['nombre']}, Correo electrónico: {value['email']}")

def registrar_producto():
    id_producto = int(input("Ingrese el ID del producto: "))
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = float(input("Ingrese el precio del producto: "))
    cantidad_producto = int(input("Ingrese la cantidad disponible del producto: "))
    productos[id_producto] = {"nombre": nombre_producto, "precio": precio_producto, "cantidad": cantidad_producto}

def ver_productos():
    print("Listado de productos:")
    for key, value in productos.items():
        print(f"ID: {key}, Nombre: {value['nombre']}, Precio: {value['precio']}, Cantidad disponible: {value['cantidad']}")

def agregar_venta(id_cliente, id_producto, cantidad):
    if id_cliente in clientes and id_producto in productos:
        if cantidad <= productos[id_producto]['cantidad']:
            venta = {"id_cliente": id_cliente, "id_producto": id_producto, "cantidad": cantidad}
            ventas.append(venta)
            productos[id_producto]['cantidad'] -= cantidad
            print("Venta registrada exitosamente.")
        else:
            print("No hay suficiente cantidad de producto disponible.")
    else:
        print("Cliente o producto no encontrado.")

def iniciar_sesion():
    id_cliente = int(input("Ingrese su ID de cliente: "))
    clave = input("Ingrese su clave: ")
    if id_cliente in clientes and clientes[id_cliente]['clave'] == clave:
        print("Inicio de sesión exitoso.")
        return id_cliente
    else:
        print("Credenciales incorrectas.")
        return None

def menu_inicio():
    print("1. Registrar cliente")
    print("2. Ver clientes")
    print("3. Registrar producto")
    print("4. Ver productos")
    print("5. Iniciar sesión")
    print("6. Salir")

def menu_compra():
    print("1. Realizar compra")
    print("2. Ver carrito de compras")
    print("3. Terminar sesión")

while True:
    menu_inicio()
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        registrar_cliente()
    elif opcion == '2':
        ver_clientes()
    elif opcion == '3':
        registrar_producto()
    elif opcion == '4':
        ver_productos()
    elif opcion == '5':
        cliente_actual = iniciar_sesion()
        if cliente_actual:
            while True:
                menu_compra()
                opcion_compra = input("Seleccione una opción: ")
                if opcion_compra == '1':
                    id_producto = int(input("Ingrese el ID del producto a comprar: "))
                    cantidad = int(input("Ingrese la cantidad a comprar: "))
                    agregar_venta(cliente_actual, id_producto, cantidad)
                elif opcion_compra == '2':
                    print("Carrito de compras:")
                    for venta in ventas:
                        print(f"Producto: {productos[venta['id_producto']]['nombre']}, Cantidad: {venta['cantidad']}")
                elif opcion_compra == '3':
                    break
                else:
                    print("Opción no válida.")
    elif opcion == '6':
        break
    else:
        print("Opción no válida.")