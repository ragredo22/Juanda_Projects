def crear_codigo_secreto(mensaje):

    repr_hex = mensaje[::2]
    repr_hex = repr_hex.hex()
    repr_bin = mensaje[::2]
    repr_bin_primero = bin(repr_bin[0])
    repr_bin_ultimo = bin(repr_bin[-1])
    resultado = str(repr_hex) + str(repr_bin) + repr_bin_primero + repr_bin_ultimo

    return resultado

mensaje_original = b"Este es un mensaje secreto"
mensaje_codificado = crear_codigo_secreto(mensaje_original)
print("Mensaje original:", mensaje_original)
print("Mensaje codificado:", mensaje_codificado)