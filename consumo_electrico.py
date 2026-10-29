# Programa usando funciones y return.

def calcular_kwh(watts, horas):
    return watts * horas / 1000

def calcular_mensual(kwh_diario, dias):
    return kwh_diario * dias

consumo_refri = calcular_kwh(150, 24)
consumo_tv = calcular_kwh(100, 5)
consumo_focos = calcular_kwh(45, 6)

consumo_diario = consumo_refri + consumo_tv + consumo_focos
print("=" * 60)
print(f"El consumo de tus aparatos eléctricos por día es de {consumo_diario:.2f} kWh.")
print(f"El consumo mensual de tus instalaciones es de {calcular_mensual(consumo_diario, 30):.2f} kWh.")
print("=" * 60)