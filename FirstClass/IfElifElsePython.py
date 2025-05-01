def recomendar_pelicula(genero, edad):

    if genero == "acción":
        if edad >= 13:
            return "Deadpool"
        else:
            return "Regreso al futuro"
    elif genero == "comedia":
        return "Aterriza como puedas"
    else:
        return "Explorar otros géneros"

genero_favorito = "acción"
edad_usuario = 26

pelicula_recomendada = recomendar_pelicula(genero_favorito, edad_usuario)

print(f"Teniendo en cuenta tu edad ({edad_usuario}) y tu género favorito ({genero_favorito}), te recomiendo la siguiente película: {pelicula_recomendada}")