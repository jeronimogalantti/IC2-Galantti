#G1
from parteD import promedio, aprobo, estadisticas
import pytest
def test_promedio():
    resultado = promedio([7, 4, 9, 10, 6])

    assert resultado == 7.2

#G2
def test_promedio_incorrecto():
    resultado = promedio([7, 4, 9, 10, 6])

    assert resultado == 7.2 #si dijera 10 habria un fallo

#G3
def test_aprobo():
    assert aprobo([8, 7, 9]) is True


def test_no_aprobo():
    assert aprobo([4, 5, 5]) is False


def test_aprobo_al_limite():
    assert aprobo([6, 6, 6]) is True

#G4
def test_estadisticas():
    resultado = estadisticas([7, 4, 9, 10, 6])

    assert resultado["promedio"] == 7.2
    assert resultado["maximo"] == 10
    assert resultado["minimo"] == 4

#G5
def test_duracion_inexistente():
    pelicula = {
        "titulo": "Dune",
        "anio": 2021,
        "director": "Denis Villeneuve"
    }

    resultado = pelicula.get("duracion", "desconocido")

    assert resultado == "desconocido"

#G6
def test_promedio_lista_vacia():
    assert promedio([]) == print("este calculo no es posible")

#G7
@pytest.mark.parametrize(
    "notas, esperado",
    [
        ([8, 7, 9], True),
        ([4, 5, 5], False),
        ([6, 6, 6], True),
    ]
)
def test_aprobo(notas, esperado):
    assert aprobo(notas) is esperado