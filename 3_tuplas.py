#coleccion constante de elemtos, inmutables, que pueden ser de un tipo o varios tipos de datos.
lista1 =[]
precio =int(input("ingrese el precio :"))
lista1.append(precio)
print(lista1)

nombre = input("ingrese el nombre :")
lista1.append(nombre)
print(lista1)



palabra = "yo me quiero mucho"
print(palabra[11])
print(len(palabra))
print(palabra[4:14])

cartera = ("lapiz", "borrador", "sacapuntas", "corrector")

print(cartera)
print(len(cartera))
print(type(cartera))
print(cartera.count("lapiz"))
print(cartera.index("borrador"))

convertida = list(cartera)
print(type(convertida))

convertida.pop(1)
print(convertida)

print(type(convertida))

cartera = tuple(convertida)

print(type(cartera))

del cartera

print(convertida)
print(type(convertida))

