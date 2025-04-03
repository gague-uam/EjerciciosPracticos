import clases.clases as c

inventario = c.Inventario()
while True:
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Buscar producto")
    print("4. Mostrar inventario")
    print("5. Salir")
        
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        codigo = int(input("Digite el codigo del producto: "))
        nombre = input("Digite el nombre del producto: ")
        precio = float(input("Digite el precio del producto: "))
        stock = int(input("Digite el stock del producto: "))
        producto = c.Producto(codigo, nombre, precio, stock)
        inventario.agregar_item(producto)
    elif opcion == "2":
        codigo = int(input("Digite el codigo del producto a eliminar: "))
        inventario.eliminar_item(codigo)
    elif opcion == "3":
        codigo = int(input("Digite el codigo del producto a buscar: "))
        producto = inventario.buscar_item(codigo)
        if producto:
            print(f"Producto encontrado: {producto}")
    elif opcion == "4":
        inventario.mostrar_inventario()
    elif opcion == "5":
        print("Nos vemos luego...")
        break
    else:
        print("Digite una opcion valida")