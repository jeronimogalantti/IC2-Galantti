from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field

app = FastAPI()


#MODELOS

class Editorial(BaseModel):
    nombre: str
    pais: str


class Libro(BaseModel):
    titulo: str
    paginas: int = Field(gt=0)
    editorial: Editorial
    disponible: bool = True


class LibroPublico(BaseModel):
    titulo: str
    paginas: int
    editorial: Editorial
    disponible: bool


class Autor(BaseModel):
    nombre: str


#DATOS

libros = [
    {
        "titulo": "El partido",
        "paginas": 310,
        "editorial": {
            "nombre": "La bocha",
            "pais": "argentina"
        },
        "disponible": True,
        "precio_costo": 10000
    },
    {
        "titulo": "Cronicas de una muerte anunciada",
        "paginas": 58,
        "editorial": {
            "nombre": "tango",
            "pais": "Argentina"
        },
        "disponible": True,
        "precio_costo": 12000
    },
    {
        "titulo": "Mi libro",
        "paginas": 249,
        "editorial": {
            "nombre": "el castillo",
            "pais": "España"
        },
        "disponible": False,
        "precio_costo": 9000
    }
]


autores = [
    {"nombre": "Fontanarrosa"},
    {"nombre": "Borges"},
    {"nombre": "Santaolalla"}
]


#B1

@app.get("/")
def inicio():
    return {"mensaje": "hola"}


#B2 y B11 

@app.get("/libros", response_model=list[LibroPublico])
def listar_libros(paginas_min: int | None = None):

    if paginas_min is None:
        return libros

    return [
        libro
        for libro in libros
        if libro["paginas"] >= paginas_min
    ]


#B3
@app.post("/libros")
def crear_libro(libro: Libro):
    libros.append(libro.model_dump())
    return libro


#B5

@app.get("/libros/{titulo}")
def buscar_libro(titulo: str):

    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            return libro

    raise HTTPException(
        status_code=404,
        detail="Libro no encontrado"
    )


#B6

@app.put("/libros/{titulo}")
def actualizar_libro(titulo: str, libro_nuevo: Libro):

    for i, libro in enumerate(libros):

        if libro["titulo"].lower() == titulo.lower():
            libros[i] = libro_nuevo.model_dump()
            return libros[i]

    raise HTTPException(
        status_code=404,
        detail="Libro no encontrado"
    )


#B7

@app.delete("/libros/{titulo}", status_code=204)
def borrar_libro(titulo: str):

    for i, libro in enumerate(libros):

        if libro["titulo"].lower() == titulo.lower():
            libros.pop(i)
            return Response(status_code=204)

    raise HTTPException(
        status_code=404,
        detail="Libro no encontrado"
    )


#B9

@app.get("/autores")
def listar_autores():
    return autores


@app.post("/autores")
def crear_autor(autor: Autor):
    autores.append(autor.model_dump())
    return autor