
numero_de_cedula = input("Dame tu numero de cedula :")


intpar = int(numero_de_cedula)
par = intpar % 2 

if par == 0:
    print("Tu numero de cedula es par")
else:
    print("Tu numero de cedula es impar")



print(numero_de_cedula)

largo = len(numero_de_cedula)
dato = numero_de_cedula[largo-1]



if dato == "2" or dato == "4" or dato == "6" or dato == "8" or dato == "0":
    print("es par")
else:
    print("Tu numero de cedula es impar")



datoint = int(dato)
print(datoint)
print(type(datoint))

if datoint == 0 or datoint == 2 or datoint == 4 or datoint == 6 or datoint == 8:
    print("es par")
else:
    print("Tu numero de cedula es impar")
    
