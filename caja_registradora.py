# Programa para una caja registradora.

# Fijamos el valor del IVA.
IVA = 0.16

# Fijamos en 'ceros' el valor de subtotal.
subtotal = 0.0

# Fijamos la cantidad de productos vendidos en 'ceros'.
articulos = 0

# Inicia ciclo 'While'.
while True:
    nombre = input("Ingresa el nombre del producto: (Escribe 'fin' si han terminado las compras: )").strip

    # Para evitar confusiones entre mayusc/minusc.
    if nombre.lower() == "fin":
        break

    # Para que no quede vacio el nombre del producto.
    if nombre == "":
        print("El nombre del producto no puede quedar en blanco, intenta de nuevo.")
        continue

    # Ingresar precios.
    while True:
        try:
            precio = float(input("Ingresa el precio del producto: $ "))

            # Para evitar que este campo quede en 'ceros'.
            if precio <= 0:
                print("En la tienda no tenemos artículos con precio $ 0")
            else:
                break
        
        # Para evitar entradas no númericas.     
        except ValueError:
            print ("Ingresa una cantidad válida.")

    # Ingresar Cantidad de artículos.
    while True:
        try:
            cantidad = input(f"Ingresa la cantidad de {nombre} que se compran.")

            # Para evitar que se capturen cantidades negativas o en ceros.
            if cantidad <= 0:
                print("Al menos debe de ingresar 1 artículo.")
            else:
                break

        # Para evitar entradas no válidas.
        except ValueError:
            print("Ingrese una cantidad entera válida")

    # Calculamos el subtotal de las compras.
    subtotal_producto = precio * cantidad

    # Acumulamos en las listas, precios y cantidades.
    subtotal += subtotal_producto
    cantidad_productos += cantidad

    # Imprimimos subtotal de productos.
    print(f"{nombre} x {cantidad} = $ {subtotal_producto:.2f}")





    