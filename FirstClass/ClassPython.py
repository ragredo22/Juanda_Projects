def gestionar_informacion(datos_personales):
    nombre, edad, ciudad = datos_personales
    nacimiento = 2025 - edad
    datos_modificados = nombre, nacimiento, ciudad
    return datos_personales, datos_modificados
datos_personales = ("Ana", 30, "madrid")
tupla_original, tupla_modificada = gestionar_informacion(datos_personales)
print("tupla original:", tupla_original)
print("tupla modificada:", tupla_modificada)