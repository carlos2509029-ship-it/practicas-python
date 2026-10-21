# Usando if, else y elif.
temperatura = float(input("\nCuál es la temperatura del motor ?: "))
if temperatura >= 90:
    print(f"\nAlerta crítica temperatura en {temperatura} grados, detener el equipo !")
elif temperatura >= 75:
    print(f"\nProgramar revisión temperatura temperatura en {temperatura} grados, y elevandose !")
else:
    print(f"\nOperación normal la temperatura del equipo es de {temperatura} grados.")
print("Inspección registrada\n")

