# Se compara el valor de referencia vs el valor ingresado por el usuario
limite = float(input("¿Cual es el límite de temperatura de trabajo del fabricante de tu equipo? "))
temperatura = float(input("Ingresa el valor actual de la temperatura de tu equipo: "))
print(temperatura > limite) # ¿La temperatura es mayor al límite?
print(temperatura < limite) # ¿La temperatura es menor al límite?
print(temperatura == limite) # ¿La temperatura es igual al límite?
print(temperatura != limite) # ¿La temperatura es diferente al límite?
if temperatura >= limite:
    print("\nALERTA CRÍTICA: detener el equipo")
elif temperatura >= limite-10:
    print("\nADVERTENCIA: programar revisión")
else:
    print("\nOperación Normal")

