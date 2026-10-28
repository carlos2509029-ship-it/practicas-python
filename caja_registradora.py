# Programa para una caja registradora.
# Asignamos el valor del IVA.
TASA_IVA = 0.16

# Asignamos valor 'cero pesos' al subtotal.
subtotal = 0.0

# Asignamos valor 'cero artículos' a articulos
articulos = 0

# Inicia ciclo 'While'.
while True:
    # Pedimos nombre del artículo
    nombre = input("\nNombre del producto: (escribe 'fin' para terminar): ").strip()

    # Evitamos que haya confusión entre mayúsculas y minúsculas y determinamos cuando acaba While.
    if nombre.lower() == "fin":
        break

    # También evitamos que no se ingrese nombre de algún producto
    if nombre == "":
        print("El nombre no puede estar vacío.")
        continue

    # Validamos precio
    while True:
        try:
            precio = float(input("Precio del producto: $"))
            # Aseguramos que no se ingrese valor $0.
            if precio <= 0:
                print("El precio debe ser mayor que cero.")
            else:
                break
        except ValueError:
            print("Ingresa un precio válido.")

    # Validamos cantidad
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            # Evitamos que se coloquen cantidades de 'cero'.
            if cantidad < 1:
                print("La cantidad debe ser al menos 1.")
            else:
                break
        except ValueError:
            print("Ingresa una cantidad entera válida.")

    # Calcular subtotal del producto
    subtotal_producto = precio * cantidad

    # Acumulamos importes y cantidades
    subtotal += subtotal_producto
    articulos += cantidad
    print(f"{nombre} x {cantidad} = ${subtotal_producto:.2f}")

# Imprimimos ticket
iva = subtotal * TASA_IVA
total = round(subtotal + iva, 2)
print(f"\nNúmero de artículos: {articulos}")
print(f"\nSubtotal:            ${subtotal:.2f}")
print(f"\nIVA (16%):           ${iva:.2f}")
print(f"\nTOTAL A PAGAR:       ${total:.2f}")

# Cobramos al cliente
while True:
    try:
        pago = float(input("¿Con cuánto paga el cliente? $"))
        if pago < total:
            faltante = total - pago
            print(f"Faltan ${faltante:.2f}. Intenta nuevamente.")
        else:
            break
    except ValueError:
        print("Ingresa una cantidad válida.")

# Calculamos el cambio
cambio = pago - total
print(f"\nPago recibido: ${pago:.2f}")
print(f"Cambio:        ${cambio:.2f}")
print("¡Gracias por su compra, vuelva pronto!")
