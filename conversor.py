# Este es un programa conversor de temperaturas de grados Cenígrados a Fahrenheit.
# y de Centigrados a Kelvin.

equipo = input("Ingresa el nombre del equipo: ")
temperatura = float(input("\nIngresa el valor en °Centigrados de la temperatura que tiene tu equipo: "))

kelvin = temperatura + 273.15
fahrenheit = temperatura * 9/5 + 32

print("\n================================CONVERSOR DE TEMPERATURA==================================    ")
print(f"=    Convertido a grados Kelvin los {temperatura} °C de tu {equipo} son equivalentes a {round(kelvin, 1)} K ")
print(f"=    Convertido a grados Fahrenheit los {temperatura} °C de tu {equipo} son equivalentes a {round(fahrenheit, 1)} °F")
print("==========================================================================================\n\n")
