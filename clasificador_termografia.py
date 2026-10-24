# Usaremos los criterios NETA más usados en termografía.
# Diferencial de 1° a 3° centígrados es considerada como falla leve se recomienda dar seguimiento.
# Diferencial de 4° a 15° centígrados es considerada como falla moderada, se recomienda reparar según criticidad y programar revisión.
# Diferencial de 16° a 40° centígrados es considerada como falla seria, requiere reparación prioritaria.
# Diferencial mayor a los 40° centígrados es considerada como falla crítica requiere acción inmediata con riesgo de falla.
# La temperatura de referencia en las líneas de transmisión ronda entre los 50 y hasta los 90°, usaremos como referencia 70° para marcar límite.

fase=input("¿Cuál fase se revisará, L1, L2 o L3? ").upper()
temp=float(input(f"¿Cuál es la temperatura de trabajo de la {fase}? "))
print(f"Vamos a revisar la fase {fase}, que tiene una temperatura de {temp}")

temp_referencia = 70
delta = temp - temp_referencia

if delta < 1:
    print(f"El delta de {fase} es de {round(delta, 1)} tu instalación trabaja a temperatura normal.")
elif delta <= 3:
    print(f"El delta de {fase} es de {round(delta, 1)} tu instalación presenta falla leve se recomienda dar seguimiento.")
elif delta <= 15:
    print(f"El delta de {fase} es de {round(delta, 1)} tu instalación presenta falla moderada se recomienda reparar según criticidad.")
elif delta <= 40:
    print(f"El delta de {fase} es de {round(delta, 1)} tu instalación presenta falla seria se requiere reparación prioritaria.")
else:
    print(f"El delta de {fase} es de {round(delta, 1)} tu instalación presenta falla crítica requiere acción inmediata.")




