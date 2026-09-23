#A1
#a)GET Queremos obtener información, sin modificarla.
#b)POST	Estamos creando un nuevo recurso.
#c)DELETE Queremos eliminar un recurso.
#d)PATCH Modificamos solamente una parte del recurso.
#e)PUT Reemplazamos completamente el recurso.
#f)PATCH Modificamos solamente un campo del recurso.

#A2
#200 OK	Pedimos un libro y la API lo devuelve correctamente.
#201 Created	Creamos un libro mediante POST.
#204 No Content	Borramos un libro correctamente y no necesitamos devolver información.
#400 Bad Request	El cliente mandó una petición incorrecta.
#404 Not Found	Buscamos un libro que no existe.
#405 Method Not Allowed	Intentamos hacer DELETE en un endpoint que solamente permite GET.
#422 Unprocessable Content	Mandamos datos que no cumplen el modelo esperado, por ejemplo "paginas": "muchas".
#500 Internal Server Error	Ocurrió un error inesperado dentro de la API.

#A3
# Los codigos iniciados en 2xx son correspondientes a un éxito, codigos iniciados en 3xx 
# corresponden a una redirección, 4xx errores del cliente y los 5xx errores del servidor

#A4
{
    "titulo": "MI LIBRO",
    "autor": "Jeronimo Galantti",
    "paginas": 310,
    "disponible": True
}
[
    {
        "titulo": "MI LIBRO",
        "autor": "Jeronimo galantti",
        "paginas": 310,
        "disponible": True
    },
    {
        "titulo": "El principito",
        "autor": "Saint-Exupery",
        "paginas": 328,
        "disponible": False
    }
]
{
    "titulo": "MI LIBRO",
    "paginas": 310,
    "disponible": True,
    "editorial": {
        "nombre": "lacasa",
        "pais": "Argentina"
    }
}
libro = {
    "titulo": "El Hobbit",
    "paginas": 310,
    "disponible": True,
    "editorial": {
        "nombre": "Minotauro",
        "pais": "España"
    }
}

#A5
#GET	Sí es idempotente porque obtener un recurso no debería modificarlo.
#POST	No es idempotente porque cada POST puede crear un recurso nuevo.
#PUT	Sí es idempotente porque reemplazar con el mismo contenido deja el mismo resultado.
#DELETE	Sí es idempotente porque una vez eliminado, repetir el DELETE mantiene el recurso eliminado

#A6
#El header sirve para aclararle al servidor en que formato estará el contenido. De esta forma será 
#capaz de interpretar el contenido

#A7
#Posibles URLs:
#GET /libros/1984
#GET /autores/Jeronimo%20Galantti
#POST /autores