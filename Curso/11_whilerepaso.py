lista =[]

i = 0
while i<5:
    n = input("escriba una palabra ")
    lista.append(n)
    print(lista)
    i = i + 1
print(lista)

i = 0
while i<5:
    n = int(input("escriba una numero "))
    lista.append(n)
    print(lista)
    i = i + 1
print(lista)


print("vamos a sumar")
i = 0
suma = 0
while i<5:
    suma = suma +lista[i]
    i = i + 1
print("el resultado se", suma)

print("vamos a multiplicar")
i = 0
multipli = 1
while i<5:
    multipli = multipli * lista[i]
    i = i + 1
print("el resultado se", multipli)






