import csv

inventario_dic = []


def VerResultados():
    for producto in inventario_dic:
        print(f"Nombre: {producto[0]}")
        print(f"Cantidad: {producto[1]}")
        print(f"Precio unitario: {producto[2]}")
        print(f"Ubicacion: {producto[3]}")
        print("=" * 20)


def cargar_inventario():
    Inventario = input("Pegar ruta del archivo .inv: ")
    print(f"\n")
    Inventario = Inventario.strip('"')
    Inventario_abrir = open(Inventario, 'r', encoding="UTF-8")
    leer_ruta1 = csv.reader(Inventario_abrir, delimiter=';')

    for linea in leer_ruta1:
        if len(linea) == 4:
            try:
                nombre, cantidad, precio_unitario, ubicacion = linea
                int(cantidad)
                name = nombre.split()[1]
                inventario_dic.append((name, cantidad, precio_unitario, ubicacion))
            except:
                print(f'El producto de "{name}" es una Cantidad con punto decimal no sera valida')
        else:
            print("Error: 404")

    Inventario_abrir.close()


def cargar_movimientos():
    Movimientos = input("Pegar ruta del archivo .mov: ")
    print(f"\n")
    Movimientos = Movimientos.strip('"')
    Movimientos_abrir = open(Movimientos, 'r', encoding="UTF-8")
    leer_ruta2 = csv.reader(Movimientos_abrir, delimiter=';')

    for linea2 in leer_ruta2:
        if len(linea2) == 3:
            nombre, cantidad, ubicacion = linea2
            nombre2 = nombre.split()[1]
            accion = nombre.split()[0]
            if accion == "agregar_stock":
                verificardor = False
                for i, producto in enumerate(inventario_dic):
                    try:
                        if nombre2 == producto[0]:
                            if ubicacion == producto[3]:
                                if int(producto[1]) > 0:
                                    resultado = int(producto[1]) + int(cantidad)
                                    inventario_dic[i] = (producto[0], resultado, producto[2], producto[3])
                                    verificardor = True
                    except:
                        print(f'El producto de "{nombre2}" es una Cantidad con punto decimal no sera valida')
                if not verificardor:
                    print(f"Error: Producto {nombre2} no encontrado en {ubicacion}")
                    linea_error = True
            elif accion == "vender_producto":
                for i, producto in enumerate(inventario_dic):
                    try:
                        if nombre2 == producto[0]:
                            if ubicacion == producto[3]:
                                if int(producto[1]) >= int(cantidad):
                                    resultado2 = int(producto[1]) - int(cantidad)
                                    inventario_dic[i] = (producto[0], resultado2, producto[2], producto[3])
                                else:
                                    print(f"Error: No existe suficente {producto} en la {ubicacion}")
                            else:
                                print(f"Error: El producto {producto} no se encuentra en {ubicacion}")
                    except:
                        print(f'El producto de "{nombre2}" es una Cantidad con punto decimal no sera valida')
            else:
                print(f"Error: El producto {producto} no existe")

        else:
            print("Error: :c")
            print(linea2)
            print(len(linea2))


def crear_informe():
    informe_filename = "Archivo_informe.txt"

    informe_file = open(informe_filename, "w")

    informe_file.write("Informe de Inventario:\n")
    informe_file.write(
        "{:<15} {:<15} {:<20} {:<15} {:<15}\n".format("Producto", "Cantidad", "Precio Unitario", "Valor Total",
                                                      "Ubicacion"))
    informe_file.write("-" * 79 + "\n")

    for producto in inventario_dic:
        cantidad = producto[1]
        precio_unitario = float(producto[2])
        ubicacion = producto[3]
        valor_total = float(cantidad) * precio_unitario
        informe_file.write(
            "{:<15} {:<15} ${:<20,.2f} ${:<14,.2f} {:<15}\n".format(producto[0], cantidad, precio_unitario, valor_total,
                                                                    ubicacion))

    informe_file.close()

    print("\033[93mInforme creado exitosamente.\033[0m")


def menu():
    while True:
        print("\033[91m" + "_" * 48)
        print(" Practica 1 - Lenguajes Formales de programación ")
        print("_" * 49 + "\033[0m")
        print("                                                 ")
        print("\033[91m# Sistema de inventario")
        print("\033[91m1. Cargar Inventario Inicial")
        print("2. Cargar Instrucciones de Movimientos")
        print("3. Mostrar Informe de Inventario")
        print("4. Salir\033[0m")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_inventario()
            VerResultados()
            print(f"\n")

        elif opcion == "2":
            cargar_movimientos()
            VerResultados()
            print(f"\n")

        elif opcion == "3":
            crear_informe()
            print("\033[93mArchivo generado.\033[0m")
            print("\n")

        elif opcion == "4":
            print("\033[93mSalir del programa.\033[0m")
            break


menu()