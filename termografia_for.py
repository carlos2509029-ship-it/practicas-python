
# Criterios de temperatura para la revisión termográfica
# Referencia: 70 °C
# Los diferenciales se evalúan respecto a la temperatura de referencia.

temp_referencia = 70

# Listas para almacenar las fases y sus temperaturas
fases = ["L1", "L2", "L3"]
temperaturas = []

# Ciclo para solicitar y evaluar la temperatura de cada fase
for fase in fases:
    temp = float(input(f"¿Cuál es la temperatura de trabajo de la fase {fase} en °C? "))

    temperaturas.append(temp)

    print(f"\nRevisando la fase {fase}, temperatura: {temp} °C")

    delta = temp - temp_referencia

    if delta < 1:
        print(f"Delta: {delta:.1f} °C. Temperatura normal.")
    elif delta <= 3:
        print(f"Delta: {delta:.1f} °C. Falla leve: se recomienda dar seguimiento.")
    elif delta <= 15:
        print(f"Delta: {delta:.1f} °C. Falla moderada: reparar según criticidad.")
    elif delta <= 40:
        print(f"Delta: {delta:.1f} °C. Falla seria: requiere reparación prioritaria.")
    else:
        print(f"Delta: {delta:.1f} °C. Falla crítica: requiere acción inmediata.")

    print("-" * 50)

# Calcular el promedio de las temperaturas
promedio = sum(temperaturas) / len(temperaturas)

# Identificar la fase con mayor temperatura
temp_maxima = max(temperaturas)
indice_maximo = temperaturas.index(temp_maxima)
fase_maxima = fases[indice_maximo]

# Mostrar resultados finales con un decimal
print("\n===== RESUMEN DE LA INSPECCIÓN =====")
print(f"Temperatura promedio: {promedio:.1f} °C")
print(f"Temperatura máxima: {temp_maxima:.1f} °C")
print(f"La fase con mayor temperatura es {fase_maxima}.")
