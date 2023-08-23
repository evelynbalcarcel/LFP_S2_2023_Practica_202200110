# LFP_S2_2023_Practica_202200110

# Manual Técnico Práctica 1

La practica esta desarrollada en el lenguaje python y utiliza la libreria `csv` para la manipulación de archivos CSV., se detalla una descripción de como esta implementado el código. 
## Estructura del Código

El código consta de varias funciones que trabajan juntas para administrar un sistema de inventario. A continuación, se presenta una descripción de las funciones y su funcionalidad:

1. **`VerResultados()`**
     Esta función muestra los resultados del inventario en la consola.
   - Funcionalidad:
     - Itera a través de `inventario_dic`.
     - Imprime el nombre del producto, la cantidad disponible, el precio unitario y la ubicación.
       
     ![image](https://github.com/evelynbalcarcel/LFP_S2_2023_Practica_202200110/assets/122993550/0b3de589-1197-4443-ba1b-238d837c562a)


2. **`cargar_inventario()`**
     Esta función carga los datos iniciales del inventario desde un archivo `.inv` y los almacena en la lista `inventario_dic`.
   - Funcionalidad:
     - Solicita al usuario que ingrese la ruta del archivo `.inv`.
     - Abre el archivo, lo lee y separa los datos en nombre, cantidad, precio unitario y ubicación.
     - Almacena la información en la lista `inventario_dic`.
       
       ![image](https://github.com/evelynbalcarcel/LFP_S2_2023_Practica_202200110/assets/122993550/94a20bf5-0765-429e-bcc4-93545802a555)


3. **`cargar_movimientos()`**
     Esta función carga y procesa los movimientos del inventario desde un archivo `.mov`, actualizando los valores de cantidad en `inventario_dic`.
   - Funcionalidad:
     - Solicita al usuario que ingrese la ruta del archivo `.mov`.
     - Abre el archivo, lee sus líneas y separa los datos en nombre, cantidad y ubicación.
     - Verifica la acción del movimiento (agregar_stock o vender_producto) y actualiza `inventario_dic` en consecuencia.
       ![image](https://github.com/evelynbalcarcel/LFP_S2_2023_Practica_202200110/assets/122993550/0bf64adb-ffe7-4e84-be48-f05acf47d745)
       La imagen tiene parte de código oculto, por lo extenso que resulata ser.


4. **`crear_informe()`**
     Esta función crea un archivo de informe llamado "Archivo_informe.txt" que muestra los detalles del inventario.
   - Funcionalidad:
     - Abre el archivo en modo escritura.
     - Itera a través de `inventario_dic`, calcula el valor total para cada producto y escribe los detalles en el informe.
       ![image](https://github.com/evelynbalcarcel/LFP_S2_2023_Practica_202200110/assets/122993550/37b25de7-8383-4f81-b718-482b80ba6998)
       
        La imagen tiene parte de código oculto, por lo extenso que resulata ser.


5. **`menu()`**
     Esta función muestra un menú de opciones al usuario y coordina la interacción con el sistema de inventario.
   - Funcionalidad:
     - Muestra el menú y permite al usuario seleccionar opciones.
     - Llama a las funciones dependiendo de la opción seleccionada.
       ![image](https://github.com/evelynbalcarcel/LFP_S2_2023_Practica_202200110/assets/122993550/2f9240fe-a34f-4af4-be1c-c5f59fce5efe)

       
## Ejecución del Programa

1. El programa comienza con la función `menu()`.
2. El usuario elige una opción del menú (cargar inventario, cargar movimientos, mostrar informe o salir).
3. Según la opción seleccionada, se llama a la función correspondiente.
4. Las funciones de carga actualizan `inventario_dic`.
5. La función de informe crea y muestra un archivo de informe.
6. El programa vuelve al menú después de completar una acción hasta que el usuario elige salir.
   ![image](https://github.com/evelynbalcarcel/LFP_S2_2023_Practica_202200110/assets/122993550/0975d27b-8af0-4b47-a4f5-9ae986c14c8c)



Para finalizar, el código ermite cargar datos iniciales, procesar movimientos y generar informes. Las funciones estan organizadas de manera que permiten una interacción sencilla con el sistema de inventario.
