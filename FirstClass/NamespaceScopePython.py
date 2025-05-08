recursos_ecosistema = {"agua": 1000, "alimento": 800}

def animal_interactua(tipo, cantidad_alimento, cantidad_agua=None):
    global recursos_ecosistema
    if tipo == "herbívoro":
        if cantidad_agua > recursos_ecosistema["agua"] or cantidad_alimento > recursos_ecosistema["alimento"]:
            print("Recursos insuficientes en el ecosistema")
            return
        recursos_ecosistema["agua"] -= cantidad_agua
        recursos_ecosistema["alimento"] -= cantidad_alimento
        print(f"Un herbívoro ha consumido {cantidad_agua} de agua y {cantidad_alimento} de alimento.")
    elif tipo == "carnívoro":
        if cantidad_alimento > recursos_ecosistema["alimento"]:
            print("Recursos insuficientes en el ecosistema")
            return
        recursos_ecosistema["alimento"] -= cantidad_alimento
        print(f"Un carnívoro ha consumido {cantidad_alimento} de alimento.")
    print("Estado actual del ecosistema:", recursos_ecosistema)

def lluvia(cantidad):
    global recursos_ecosistema
    recursos_ecosistema["agua"] += cantidad
    print(f"¡Ha llovido! Se añadieron {cantidad} unidades de agua al ecosistema.")

print("Inicio del día en el ecosistema:", recursos_ecosistema)
animal_interactua("herbívoro", 100, 200)
animal_interactua("carnívoro", 50)
lluvia(200)
print("Fin del día en el ecosistema:", recursos_ecosistema)