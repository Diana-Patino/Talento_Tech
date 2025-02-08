#Tratando de aprender a subir a la nube lo que hago aqui
#segundo intento
#tercero
#cuarto
#quinto
print("febrero 2")

#en el dicionario cada dato tiene llave

persona = {"diana":"patiño","astrid":"martinez","edad":33,"residencia":"bello",2:"hola"}
print(persona["diana"])
print(persona[2])

#para leerlo mejor separamos en cada linea 
persona = {
            "diana":"patiño",
            "astrid":"martinez",
            "edad":33,
            "residencia":"bello",
            2:"hola"
            }

#metodos asociados a los dicionarios

#persona.clear()
#print(persona)

dic2= persona.copy()
print(dic2)

# !!!!!!!!!!!!!!!!!!            .fromkeys() de una tupla devuelve un dic con llave y valor asignado
#x = ("a", "b", "c", "d")
#y = (1)
#dic3 = dict.fromkeys()
#print(dic3)

print(persona.get("diana"))
nombreEmpleado = persona.get("diana")
print(nombreEmpleado)
print(persona["diana"])

#actualizar el valor de la llave
persona["diana"] = "Astrid"
print(persona["diana"])

# me imprime las parejas como item dentro de una tupla que esta dentro de una lista
a = persona.items()
print(a)


print(persona.keys()) #devuelve las llaves dentro de una tupla
print(persona.values()) #devuelve las valores dentro de una tupla

persona.pop("diana") #elimina elemento
print(persona) 
persona.popitem() #elimina el ultimo elemento

persona.update({"color":"azul"}) #agreda un elemento al diccionario
print(persona) 

#persona.setdefault()
#print(persona) 

persona["gata2"] = "sombra" #agreda un elemento al diccionario

print(persona) 

del persona["color"] #elimina elemento
print(persona) 
