def crea_tablero(filas, columnas):
    tablero = [None]*filas
    for f in range(filas):
        tablero[f] = ["."]*columnas
    return tablero
tablero = crea_tablero(6, 7)

def mostrar_tablero(tablero):
    print(0, 1, 2, 3, 4, 5, 6)