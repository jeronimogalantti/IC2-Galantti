#E1

from fastapi.testclient import TestClient
from ParteB import app

client = TestClient(app)


def test_listar_libros():
    respuesta = client.get("/libros")

    assert respuesta.status_code == 200

#E2

def test_crear_libro_sin_paginas():
    libro = {
        "titulo": "Libro sin paginas",
        "editorial": {
            "nombre": "Editorial de prueba",
            "pais": "Argentina"
        },
        "precio_costo": 1000
    }

    respuesta = client.post("/libros", json=libro)

    assert respuesta.status_code == 422

#E3

def test_crear_libro_valido():
    libro = {
        "titulo": "Libro de prueba valido",
        "paginas": 120,
        "editorial": {
            "nombre": "Editorial de prueba",
            "pais": "Argentina"
        },
        "disponible": True,
        "precio_costo": 1500
    }

    respuesta = client.post("/libros", json=libro)

    assert respuesta.status_code in (200, 201)

def test_crear_libro_invalido():
    libro = {
        "titulo": "Libro invalido",
        "paginas": -10,
        "editorial": {
            "nombre": "Editorial de prueba",
            "pais": "Argentina"
        },
        "disponible": True,
        "precio_costo": 1500
    }

    respuesta = client.post("/libros", json=libro)

    assert respuesta.status_code == 422

#E4

def test_crear_libro_y_verlo_en_lista():
    libro = {
        "titulo": "Libro creado desde test",
        "paginas": 200,
        "editorial": {
            "nombre": "Editorial de prueba",
            "pais": "Argentina"
        },
        "disponible": True,
        "precio_costo": 2500
    }

    respuesta_post = client.post("/libros", json=libro)

    assert respuesta_post.status_code in (200, 201)

    respuesta_get = client.get("/libros")

    assert respuesta_get.status_code == 200

    libros = respuesta_get.json()

    titulos = [libro["titulo"] for libro in libros]

    assert "Libro creado desde test" in titulos