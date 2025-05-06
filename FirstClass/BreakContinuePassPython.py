def simulador_alarma(tiempo_total):

    segundo_actual = 0
    while segundo_actual < tiempo_total:
        segundo_actual += 1

        if segundo_actual % 10 == 0:
            print(f"Omitiendo alarma en segundo {segundo_actual}")
            continue  # Omite la acción de la alarma para este segundo

        print(f"Alarma activada, segundo actual: {segundo_actual}")

        if segundo_actual == tiempo_total:
            print(f"Alarma desactivada a los {segundo_actual} segundos")
            break

simulador_alarma(21)