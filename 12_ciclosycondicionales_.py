
"""
frutas = ["limon", "manzana", "pera "]
print(frutas)

for x in frutas:
    print(x)


frutas = ["limon", "manzana", "pera "]
i = 0
while i<3:
    print(frutas[i])
    i = i + 1

persona = {"nombre":"Diana","apellido":"patiño","edad":"33"}
palabra = "sombrita"



numero= int(input("dame un numero para multiplicar :"))
#comento
for i in range(1,11):
    print(i*numero)
   

i = 1
for i in range(1, 11):
    print("vamos a hacer la tabla de :", i)
    for j in range(1,11):
        print(i, "x", j, "=",i*j)
"""

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
    







#productos.setdefault(agregarproducto)
#productos[agregarproducto] = cantidaddelproducto
#print(productos)
"""
if eleccion == str(5):
    agregarproducto = input("Nombre del producto a agregar ")
    cantidaddelproducto= int(input("cantidad a agragar del producto"))
    productos[agregarproducto] = cantidaddelproducto
print(productos)"""
