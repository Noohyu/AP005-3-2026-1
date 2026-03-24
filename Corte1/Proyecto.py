# 1. Mensaje de bienvenida 
print("========================================")
print("  Bienvenido al Sistema de Inventario   ")
print("========================================")

# 7. Tupla para manejar información fija (Categorías permitidas)
CATEGORIAS_VALIDAS = ("Electrónica", "Hogar", "Alimentos", "Ropa")

# 6. Lista para almacenar los productos
inventario = []

# 2. Menú principal mediante un ciclo while 
continuar = True
while continuar:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    
    # 3. Uso de input() para capturar información 
    opcion = input("\nSeleccione una opción: ")

    # 5. Estructuras condicionales if, elif, else 
    if opcion == "1":
        print("\n--- Agregar Nuevo Producto ---")
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        
        # 4. Conversión de tipos (int/float) y 10. Validación de datos 
        try:
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Error: El precio y la cantidad deben ser valores numéricos.")
            continue

        print(f"Categorías disponibles: {CATEGORIAS_VALIDAS}")
        categoria = input("Categoría: ")

        # 8. Diccionario para representar cada producto 
        # 34-40. Información mínima de cada producto 
        nuevo_producto = {
            "código": codigo,
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
            "categoría": categoria
        }
        
        # 29. Funcionalidad: Agregar producto 
        inventario.append(nuevo_producto)
        print("¡Producto agregado con éxito!")

    elif opcion == "2":
        # 30. Funcionalidad: Mostrar todos los productos 
        print("\n--- Lista de Inventario ---")
        if not inventario:
            print("El inventario está vacío.")
        else:
            # 9. Uso de ciclo for para recorrer la información 
            for prod in inventario:
                print(f"ID: {prod['código']} | Nombre: {prod['nombre']} | "
                      f"Precio: ${prod['precio']} | Cant. {prod['cantidad']} | "
                      f"Cat: {prod['categoría']}")

    elif opcion == "3":
        # 31. Funcionalidad: Buscar producto 
        busqueda = input("\nIngrese el código del producto a buscar: ")
        encontrado = False
        for prod in inventario:
            if prod["código"] == busqueda:
                print(f"Resultado: {prod}")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")

    elif opcion == "4":
        # 32. Funcionalidad: Eliminar producto 
        eliminar = input("\nIngrese el código del producto a eliminar: ")
        for i in range(len(inventario)):
            if inventario[i]["código"] == eliminar:
                inventario.pop(i)
                print("Producto eliminado correctamente.")
                break
        else:
            print("No se encontró el código especificado.")

    elif opcion == "5":
        # 26. Opción para salir y 33. Funcionalidad salir 
        print("Saliendo del sistema... ¡Hasta luego!")
        continuar = False

    else:
        print("Opción no válida, intente de nuevo.")
