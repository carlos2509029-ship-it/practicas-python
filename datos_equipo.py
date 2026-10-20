# Datos de un equipo industrial
equipo = "Compresor de aire"
potencia_hp = 55
temperatura_trabajo = 75.5
en_operacion = True
horas_dia = 15
dias = 30
horas_mes = horas_dia * dias
potencia_kw = potencia_hp * 0.746

print(equipo)
print(potencia_hp)
print(type(equipo))
print(type(potencia_hp))
print(type(temperatura_trabajo))
print(type(en_operacion))
print(f"El {equipo} tiene {potencia_hp} hp y opera a {temperatura_trabajo} °C")
print(f"El {equipo} trabaja {horas_mes} horas mensualmente")
print(f"La potencia del {equipo} es de {potencia_kw} kw")
print(f"Redondeados son: {round (potencia_kw, 1)}")