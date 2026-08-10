#D1
def promedio(notas):
    if len(notas) == 0:
        return print("este calculo no es posible")
    return sum(notas) / len(notas)

notas1 = [7, 4, 9, 3, 6]
notas2 = [8, 8, 9, 7, 10]
print(promedio(notas1))
print(promedio(notas2))

#D2
def aprobo(notas, minimo=6):
    if promedio(notas) >= minimo:
        return True
    else:
        return False

print(aprobo(notas1))
print(aprobo(notas2))

#D3
def estadisticas(notas):
    return {
        "promedio": promedio(notas),
        "maximo": max(notas),
        "minimo": min(notas)
    }
print(estadisticas(notas1))
print(estadisticas(notas2))

#D5
promedio([]) #se soluciono con un if de un mensaje que dice que no es posible la operacion

#D6 
def reporte(notas):
    datos = estadisticas(notas)
    return (
        f"Promedio: {datos['promedio']} | "
        f"Máximo: {datos['maximo']} | "
        f"Mínimo: {datos['minimo']}"
    )
print(reporte(notas1))