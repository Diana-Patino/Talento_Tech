Ese es mi primer proyecto git y github
productos = {}

while True:
    print("Que quieres realizar? :")
    print("1 - Agregar producto")
    print("2 - Vender producto")
    print("3 - Mostrar inventario")
    print("4 - salir")
    
    print("Elije una opción :")
    eleccion = input("")

    productos.keys()
    llaves= list(productos.keys())
   
    
    if eleccion == str(1):
        agregarproducto = input("Nombre del producto a agregar ")
        cantidaddelproducto= int(input("cantidad a agregar del producto"))
        if agregarproducto in llaves:
            productos[agregarproducto] += cantidaddelproducto
        else:
            productos[agregarproducto] = cantidaddelproducto
    print(productos)
    print("gracias")


    if eleccion == str(2):
        productoavender = input("Nombre del producto a vender ")
        cantidadavender= int(input("cantidad a vender del producto"))
        if productoavender in llaves:
            productos[productoavender] -= cantidadavender
        else:
            print("no hay stock")
    print(productos)

    if eleccion == str(3):
        print(productos)

    if eleccion == str(4):
        print("fin")
        break
    
