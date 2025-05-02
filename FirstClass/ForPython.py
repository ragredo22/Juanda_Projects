def añadir_tarea(tarea):

    archivo = open("tareas.txt","r")
    tareas = archivo.read().splitlines()
    tareas += [tarea]
    return tareas

def gestionar_tareas(tareas):

    num_tareas = 0
    print("Tareas pendientes de realizar:")
    for tarea_pendiente in tareas:
        num_tareas += 1
        print(f"{num_tareas}.{tarea_pendiente}")
    print(f"Hay {num_tareas} tareas pendientes de realizar")

tareas = añadir_tarea("Pagar la factura de internet.")
gestionar_tareas(tareas)