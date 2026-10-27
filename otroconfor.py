# Programa que evalúa la temperatura en las líneas de distribución.
# Usaremos ciclo 'for' y condicional 'if'.

# Establecemos de forma aibitraria la temperatura normal en 70°C.
temp_norm = 70

# Abrimos lista para las fases.
fases = ["Fase 1", "Fase 2", "Fase 3"]

# Abrimos lista vacía para las temperaturas que serán ingresadas.
temperaturas = []

# Inicia ciclo 'for'.
for fase in fases:
    temp = float(input(f"Cual es la temperatura en la fase {fase}? :"))
    print(f"La temperatura en la fase {fase} es de {temp}°C.")
    temperaturas.append(temp)
    # Establecemos el delta.
    delta = temp - temp_norm

    # Inicia condicional 'if'.
    if delta <=1:
        print(f"El Delta es de {delta}°C, la temperatura es normal.")
    elif delta <= 3:
        print(f"El Delta es de {delta}°C, el sistema presenta una falla leve.")
    elif delta <= 15:
        print(f"El Delta es de {delta}°C, el sistema presenta falla moderada.")
    elif delta <= 40:
        print(f"El Delta es de {delta}°C, el sistema presenta falla seria.")
    else:
        print(f"El delta es de {delta}°C, la falla es crítica.")

# Calculamos el promedio de las temperatruras ingresadas.
promedio = sum(temperaturas) / len(temperaturas)

# Buscamos cuál fue la temperatura máxima.
temp_max = max(temperaturas)

# Buscamos a cuál fase corresponde esa temperatura.
indice_maximo = temperaturas.index(temp_max)
fase_maxima = fases[indice_maximo]

print(f"\nEl promedio de las temperaturas ingresadas es {promedio:.1f}°C.")
print(f"La temperatura máxima ingresada es {temp_max}°C y corresponde a la fase {fase_maxima}.")