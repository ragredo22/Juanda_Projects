def crea_tablero(filas, columnas):
    tablero = [None]*filas
    for f in range(filas):
        tablero[f] = ["."]*columnas
    return tablero
tablero = crea_tablero(6, 7)