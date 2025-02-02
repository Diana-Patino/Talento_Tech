frutas = ["diana","patino","sabado","hola","hola"]
tamaño = len(frutas)
print(frutas)
frutas.append("mario")#agrega un elemento al final de la lista
print(frutas)
frutas[1]="fresa" #reemplaza el valor de una variable
print(frutas)
frutas.insert(1,"corozo")#inserta el valor de una variable, se mete en medio
print(frutas)
frutas.clear()#elimina todos los elementos de una lista
print(frutas)
#del frutas #elimino la lista
#print(frutas)

frutas22 = frutas.copy()
print(frutas22)
frutas22.append("trece")
print(frutas)
print(frutas22)
frutas33=frutas
frutas33.append("hola")
print(frutas33) 
print(frutas)
cantidad = frutas.count("hola")#cuenta las veces que esta el parametro en la lista
print(cantidad)
cantidad2 = frutas33.count("hola")
print(cantidad2)
flores = ["rosa", "margarita","eugenio","casa","penca"]
frutas.extend(flores)#extiende la lista frutas poniendo el contenido de la lista flores
print(frutas)
 
print(frutas.index("hola"))#me dice en que posicion esta un elemento, si esta vairas veces solo dice la primera posicion
print(frutas)

frutas.pop()#elimina el ultimo de la lista
print(frutas)
frutas.pop(1)#elimina el elemento en la posicion que le digo
print(frutas)
frutas.remove("casa")#elimina el primer elemento igual al que le digo que se encuentre en la lista
print(frutas)
frutas.reverse()#la voltea
print(frutas)
frutas.sort()#lo pone en orden alfabetifo. numeros de mayos a menor, solo funciona si son el mismo tipo de datos
print(frutas)

flores = ["rosa","mariesito", "margarita","eugenio","casa","penca"]

print(flores[1:3])#rango de impresion hasta el inmediatamente anterior
print(flores[1:])#imprime del numero en adelante
print(flores[:3])#imprime del numero hacia atras, excluyendo el numero 

flores.extend("dianita")
print(flores)
print(flores.index("a"))
