# Usando operdores lógicos y condicionales
limitetemp = 80
limitevibr = 7.1
temperatura = int(input("\nIngresa la temperatura del motor: "))
vibracion = float(input("Ingresa las vibraciones registradas: "))
if temperatura > 80 and vibracion > 7.1:
    print(f"Falla inminente, temperatura mayor de {limitetemp} y vibraciones arriba de {limitevibr}, revisar el equipo.")
elif temperatura > 80 or vibracion > 7.1:
    print("Revisar urgente, uno de los dos parametros críticos fuera de rango.")
else:
    print("Parametros de temperatura y vibraciones normales")