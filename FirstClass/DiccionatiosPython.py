def agregar_experiencia(perfil_laboral, nueva_experiencia):
    perfil_laboral["experiencias"] += [nueva_experiencia]
    return perfil_laboral

def generar_cv_reducido(perfil_laboral):
    print()