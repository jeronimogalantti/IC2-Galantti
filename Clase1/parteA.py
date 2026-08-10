#A1
notas = [7, 4, 9, 10, 6]
promedio = sum(notas) / len(notas)
print ("promedio: ", promedio)
if promedio >= 6:
    print ("aprobó")
else:
    print("no aprobó")

#A2 al principio falla porque es un variable numérica por un string
cantidad = "5"
precio = 100
print("Tipo de cantidad:", type(cantidad))
print("Tipo de precio:", type(precio))
print("Resultado original:", cantidad * precio)
cantidad = int(cantidad)
resultado = cantidad * precio
print("Resultado corregido:", resultado)

#A3
Celsius = 30
Fahrenheit = Celsius * 9/5 + 32
print ("temperatura en celsius: ", Celsius, "°C", "temperatura en fahrenheit: ", Fahrenheit, "°F")

#A4
print("promedio con un solo decimal: ", round(promedio, 1))

#A5
edad = 17
if edad >= 18:
    print("mayor de edad")
else:
    print("menor de edad")

#A6
pares = 0
impares = 0
for numero in range(0, 30):
    if numero % 2 == 0:
        pares+= 1
    else:
        impares+=1
print("cantidad de pares: ", pares)
print("cantidad de impares: ", impares)

#A7
kilometros = 3
millas = kilometros * 0.621371
pies = millas * 5280
print(kilometros, "Km")
print(millas, "M")
print(pies, "Ft")
