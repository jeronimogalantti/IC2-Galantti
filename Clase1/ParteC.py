#C1
pelicula = {
    "título": "Pulp Fiction",
    "Año": 1994,
    "Director": "Quentin Tarantino",
}
print(pelicula["título"])

#C2
pelicula["Puntaje"] = 8.7
pelicula["Año"] = 1995
print(pelicula)

#C3
duracion = pelicula.get("duracion", "desconocido")
print("duracion: ", duracion)

#C4
peliculas = [
    {
        "titulo": "avatar",
        "año": 2005,
        "director": "james cameron",
    },
    {
        "titulo": "the dark knight",
        "año": 2008,
        "director": "cristopher nolan",
    },
    {
        "titulo": "spiderman",
        "año": 2002,
        "director": "sam raimy",
    }
    
]
for pelicula in peliculas:
    print(pelicula["titulo"])

#C5
director_buscado = "spielberg"
encontradas = False
for pelicula in peliculas:
    if director_buscado in pelicula["director"]:
        print(pelicula["titulo"])
        encontradas = True
if not encontradas:
    print("no se encontraron peliculas de ese director")

#C6
peli1 ={
    "titulo": "dune",
    "año": 2021
}
peli2 ={
    "puntaje": 8.5,
    "año": 2024
}
combinado = peli1 | peli2 #de esta forma gana el valor del diriccionario de la derecha
print(combinado)
peli2.update(peli1) #esto actualiza peli2 y agrega los valores de peli 1 y remplaza el repetido
print(peli2)

#C7
frase = "la pelota no se la mancha"
palabras = frase.split()
conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1
print(conteo)

#C8
inventario = {
    "producto1": {
        "precio": 50,
        "stock": 100
    },
    "producto2": {
        "precio": 150,
        "stock": 200
    },
    "producto3": {
        "precio": 350,
        "stock": 500 
    }
}
precio_producto2 = inventario["producto2"]["precio"]
print("precio del segundo producto: ", precio_producto2)