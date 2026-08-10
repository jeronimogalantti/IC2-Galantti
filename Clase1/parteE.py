#E1
with open("Clase1/peliculas.csv", "r") as archivo:
    for linea in archivo:
        print(linea)

#E2
suma = 0 
with open("Clase1/peliculas.csv", "r") as archivo:
    archivo.readline()

    for linea in archivo:
        titulo, año, puntaje, genero = linea.strip().split(",")

        puntaje = float(puntaje)

        suma += puntaje

print(suma)

#E3
cantidad = 0
suma = 0
mejor_puntaje = 0
mejor_pelicula = ""

with open("Clase1/peliculas.csv", "r") as archivo:
    archivo.readline()

    for linea in archivo:
        titulo, año, puntaje, genero = linea.strip().split(",")

        puntaje = float(puntaje)

        cantidad += 1
        suma += puntaje

        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_pelicula = titulo

promedio = suma / cantidad

print("Cantidad de películas:", cantidad)
print("Puntaje promedio:", promedio)
print("Mejor puntuada:", mejor_pelicula)

#E4
genero_buscado = "ciencia ficcion"
with open("Clase1/peliculas.csv", "r") as archivo:
    encabezado = archivo.readline()
    with open("Clase1/filtradas.csv", "w") as salida:
        salida.write(encabezado)

        for linea in archivo:
            titulo, año, puntaje, genero = linea.strip().split(",")

            if genero == genero_buscado:
                salida.write(linea)

#E5
sumas = {}
cantidades = {}

with open("Clase1/peliculas.csv", "r") as archivo:
    archivo.readline()

    for linea in archivo:
        titulo, anio, puntaje, genero = linea.strip().split(",")

        puntaje = float(puntaje)

        sumas[genero] = sumas.get(genero, 0) + puntaje
        cantidades[genero] = cantidades.get(genero, 0) + 1


promedios = {}

for genero in sumas:
    promedios[genero] = sumas[genero] / cantidades[genero]


print(promedios)