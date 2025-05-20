def Air_qualify (city, username):

    PolCali = "The index of pollution in this city is 24 and it's color is green"
    InPolCali = "air quality is satisfactory also air poluttion poses little or no risk."
    InfoCali = "Cali is a city full of color and flavor, and the heavenly branch has many activities branch has many activities and experienses"
    print(PolCali, InPolCali, InfoCali)


print("ingrese ciudad")
city = input()

print("Ingrese Usuario")
usuario = input()

if city == "Cali" :
    print(Air_qualify(city, usuario))
elif city == "Bello":
    print(Air_qualify(city, usuario))
elif city == "Medellin":
    print(Air_qualify(city, usuario))
else:
    print("ingresa una respuesta valida")

print("papi hago esto por cumplir porque hoy estoy muy ocupado y estoy mareado")