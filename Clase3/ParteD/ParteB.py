import os
from contextlib import asynccontextmanager

import psycopg
from psycopg.rows import dict_row
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field


# CONEXIÓN A LA BASE

def conectar():
    return psycopg.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        dbname=os.environ["DB_NAME"],
        connect_timeout=3,
    )


@asynccontextmanager
async def lifespan(app):
    # Se ejecuta una vez, al arrancar la API: crea la tabla si no existe
    with conectar() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS libros (
                id SERIAL PRIMARY KEY,
                titulo TEXT NOT NULL,
                paginas INTEGER NOT NULL,
                editorial_nombre TEXT NOT NULL,
                editorial_pais TEXT NOT NULL,
                disponible BOOLEAN NOT NULL DEFAULT TRUE
            )
            """
        )
    yield


app = FastAPI(lifespan=lifespan)


# MODELOS

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


# DATOS (los que siguen en memoria)

libros = [
    {
        "titulo": "El partido",
        "paginas": 310,
        "editorial": {"nombre": "La bocha", "pais": "argentina"},
        "disponible": True,
        "precio_costo": 10000
    },
    {
        "titulo": "Cronicas de una muerte anunciada",
        "paginas": 58,
        "editorial": {"nombre": "tango", "pais": "Argentina"},
        "disponible": True,
        "precio_costo": 12000
    },
    {
        "titulo": "Mi libro",
        "paginas": 249,
        "editorial": {"nombre": "el castillo", "pais": "España"},
        "disponible": False,
        "precio_costo": 9000
    }
]

autores = [
    {"nombre": "Fontanarrosa"},
    {"nombre": "Borges"},
    {"nombre": "Santaolalla"}
]


# ENDPOINTS

@app.get("/")
def inicio():
    return {"mensaje": "hola"}


@app.get("/salud")
def salud():
    try:
        with conectar() as conn:
            conn.execute("SELECT 1")
        return {"base": "ok"}
    except Exception as e:
        return {"base": "error", "motivo": str(e)}


@app.get("/libros", response_model=list[LibroPublico])
def listar_libros(paginas_min: int | None = None):
    consulta = """
        SELECT titulo, paginas, editorial_nombre, editorial_pais, disponible
        FROM libros
    """
    params = ()
    if paginas_min is not None:
        consulta += " WHERE paginas >= %s"
        params = (paginas_min,)
    consulta += " ORDER BY id"

    with conectar() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(consulta, params)
            filas = cur.fetchall()

    return [
        {
            "titulo": f["titulo"],
            "paginas": f["paginas"],
            "editorial": {
                "nombre": f["editorial_nombre"],
                "pais": f["editorial_pais"],
            },
            "disponible": f["disponible"],
        }
        for f in filas
    ]


@app.post("/libros")
def crear_libro(libro: Libro):
    with conectar() as conn:
        conn.execute(
            """
            INSERT INTO libros
                (titulo, paginas, editorial_nombre, editorial_pais, disponible)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                libro.titulo,
                libro.paginas,
                libro.editorial.nombre,
                libro.editorial.pais,
                libro.disponible,
            ),
        )
    return libro


@app.get("/libros/{titulo}")
def buscar_libro(titulo: str):
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            return libro

    raise HTTPException(status_code=404, detail="Libro no encontrado")


@app.put("/libros/{titulo}")
def actualizar_libro(titulo: str, libro_nuevo: Libro):
    for i, libro in enumerate(libros):
        if libro["titulo"].lower() == titulo.lower():
            libros[i] = libro_nuevo.model_dump()
            return libros[i]

    raise HTTPException(status_code=404, detail="Libro no encontrado")


@app.delete("/libros/{titulo}", status_code=204)
def borrar_libro(titulo: str):
    for i, libro in enumerate(libros):
        if libro["titulo"].lower() == titulo.lower():
            libros.pop(i)
            return Response(status_code=204)

    raise HTTPException(status_code=404, detail="Libro no encontrado")


@app.get("/autores")
def listar_autores():
    return autores


@app.post("/autores")
def crear_autor(autor: Autor):
    autores.append(autor.model_dump())
    return autor