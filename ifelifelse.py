# Usando if, else y elif.
temperatura = float(input("\nCuál es la temperatura del motor?: "))
if temperatura >= 90:
    print(f"\nAlerta crítica temperatura en {temperatura} grados, detener el equipo!")
elif temperatura >= 75:
    print(f"\nProgramar revisión temperatura en {temperatura} grados, y elevándose!")
else:
    print(f"\nOperación normal la temperatura del equipo es de {temperatura} grados.")
print("Inspección registrada\n")

