# Usando operadores lógicos y condicionales
limite_temp = 80
limite_vibr = 7.1
temperatura = float(input("\nIngresa la temperatura del motor: "))
vibracion = float(input("Ingresa las vibraciones registradas: "))
if temperatura > 80 and vibracion > 7.1:
    print(f"Falla inminente, temperatura mayor de {limite_temp} y vibraciones arriba de {limite_vibr}, revisar el equipo.")
elif temperatura > 80 or vibracion > 7.1:
    print("Revisar urgente, uno de los dos parámetros críticos fuera de rango.")
else:
    print("Parametros de temperatura y vibraciones normales")