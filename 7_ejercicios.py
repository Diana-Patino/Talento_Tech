#Ejercicio en clase


nombre = ["Ana", "luis", "carlos", "maria"]
edades = (25, 30, 22, 28)
ciudades = {"Madrid","Barcelona", "sevilla"}

calificaciones = {"Ana":8.5, "luis":7.0, "carlos":9.0, "maria": 6.5}

print("Tercer nombre" , nombre[2])

list(edades)
print("Tercer edad", edades[2])


unidas = zip(nombre, edades)
print(list(unidas))

ciudades.add("Valencia")
print(ciudades)

enlistar = calificaciones.values()
print(list(enlistar))
