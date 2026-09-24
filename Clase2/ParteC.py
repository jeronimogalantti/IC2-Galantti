#C1, C2, C4, C6 Y C7

import requests

url = "http://127.0.0.1:8000/libros"
try:
    respuesta = requests.get(
        "http://127.0.0.1:8000/libros",
        timeout=1
    )

    print(respuesta.status_code)

except requests.exceptions.Timeout:
    print("La petición tardó demasiado")

except requests.exceptions.ConnectionError:
    print("No se pudo conectar con la API")

libro = {
    "titulo": "Pajaros",
    "paginas": 412,
    "editorial": {
        "nombre": "el establo",
        "pais": "Estados Unidos"
    },
    "disponible": True,
    "precio_costo": 15000
}

respuesta = requests.post(url, json=libro)

print("POST:")
print(respuesta.status_code)
print(respuesta.json())

respuesta = requests.get(url)
if respuesta.status_code == 200:
    print("La consulta fue exitosa")
    print(respuesta.json())

elif respuesta.status_code == 404:
    print("El recurso no existe")

elif respuesta.status_code == 422:
    print("Los datos enviados no son válidos")

else:
    print("Código recibido:", respuesta.status_code)

print("GET:")
print(respuesta.status_code)
print(respuesta.json())

#C3

#/docs funciona porque Swagger genera la petición HTTP con la URL, headers y body JSON 
# correctamente. En mi script tengo que hacer lo mismo; usando requests.post(url, json=libro), 
# requests convierte el diccionario a JSON y establece el Content-Type: application/json.
# Además, la URL y el puerto deben coincidir con los del servidor FastAPI."

#C5

url = "http://127.0.0.1:8000/libros/Pajaros"

libro_nuevo = {
    "titulo": "Pajaros - Edición nueva",
    "paginas": 500,
    "editorial": {
        "nombre": "el establo",
        "pais": "Estados Unidos"
    },
    "disponible": True,
    "precio_costo": 18000
}

respuesta = requests.put(url, json=libro_nuevo)

print(respuesta.status_code)
print(respuesta.json())


url = "http://127.0.0.1:8000/libros/El%20partido"

respuesta = requests.delete(url)

print(respuesta.status_code)

#C8
import requests

with requests.Session() as session:

    respuesta = session.get(
        "http://127.0.0.1:8000/libros"
    )

    print(respuesta.status_code)

    respuesta = session.get(
        "http://127.0.0.1:8000/autores"
    )

    print(respuesta.status_code)