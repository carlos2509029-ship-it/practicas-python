# Este es un programa conversor de temperaturas de grados Farenheit a Cenigrados.
# y de Kelvin a Centigrados.

equipo = input("Ingresa el nombre del equipo: ")
temperatura = float(input("\nIngresa el valor de la temperatura que tiene tu equipo: "))

kelvin = temperatura + 273.15
farenheit = temperatura * 9/5 + 32

print("\n================================COMVERSOR DE TEMPERATURA==================================    ")
print(f"=    Convertido a grados Kelvin los {temperatura} °C de tu {equipo} son equivalentes a {round(kelvin, 1)} °K      =")
print(f"=    Convertido a grados Farenheit los {temperatura} °C de tu {equipo} son equivalentes a {round(farenheit, 1)} °K    =")
print("==========================================================================================\n\n")
