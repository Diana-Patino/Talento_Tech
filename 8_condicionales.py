
#python agrupa las instrucciones segun la identacion, alineacion de columnas



edad= int(input("cual es tu edad :"))

if edad >= 18:
    print("Acceso concedido")
    print("Bienvenido")
else:
    print("Acceso denegado")

print("Gracias")



color = str(input("Cual e tu color favorito :"))

if color in ("amarillo", "azul", "rojo"):
    print("Hace parte de los colores primarios")
elif color in ("blanco", "negro"):
    print("No se clasifica como un color")
else:
    print("No hace parte de los colores primarios")
