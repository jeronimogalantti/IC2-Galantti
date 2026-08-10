#B1
canciones = ["La bestia pop", "Lobo, estas?", "Fuegos de octubre", "jijiji", "Flight 956"]
print("playlist: ", canciones)
print("primera cancion:", canciones[0])
print("ultima cancion: ", canciones[-1])

#B2
canciones.append("La hija del fletero")
canciones.append("Cruz diablo")
print("cantidad de canciones: ", len(canciones))

#B3
puntajes = [120, 45, 300, 80, 210]
mayor = puntajes[0]
menor = puntajes[0]
prom = sum(puntajes) / len(puntajes)
for puntaje in puntajes:
    if puntaje > mayor:
        mayor = puntaje
    if puntaje < menor:
        menor = puntaje

print("el mayor es: ", mayor)
print("el menor es: ", menor)
print("el promedio es: ", prom)
print("Mayor con max():", max(puntajes))
print("Menor con min():", min(puntajes))

#B4
mayores_a_100 = []
for puntaje in puntajes:
    if puntaje > 100:
        mayores_a_100.append(puntaje)

print("lista mayores de 100: ", mayores_a_100)

#B5
ranking = sorted(puntajes, reverse=True)
print("lista de mayor a menor: ", ranking)

#B6
playlist_invertida = canciones[::-1]
print("playlist invertida: ", playlist_invertida)

#B7
numeros = [3, 5, 3, 8, 5, 1, 8, 8]
sin_repetidos = list(set(numeros))
print("lista original: ", numeros)
print("lista sin repetidos: ", sin_repetidos)

#B8 porque en una lista de 10 se pueden armar 8 promedios de 3 datos cada uno
lecturas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
promedios = []
for i in range (len(lecturas) -2):
    ventana = lecturas[i : i+3]
    promedio = sum(ventana) / len(ventana)
    promedios.append(promedio)
print("lecturas: ", lecturas)
print("promedios moviles:", promedios)