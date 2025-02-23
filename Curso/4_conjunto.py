
conjunto={"diana","astrid"}

print(conjunto)#se dechara cpn {}
#no puede tener elementos repetidos
#no tiene orden de posicion - ubicacion

conjunto.add("15")
print(conjunto)
conjunto.add(True)
#toma 1 como verdadero
#toma 0 como falso"
conjunto.add(1)
print(conjunto)
conjunto.add(0)
print(conjunto)
conjunto.add(False)
print(len(conjunto))

conjunto.clear()
print(conjunto)
conjunto2= conjunto.copy()
print(conjunto2)

conjunto= {"rojo","verde","amarillo","mazda"}
conjunto2= {"chevrolet","audi","renault","mazda"}
#print(conjunto.difference(conjunto2))
#print(conjunto2.difference(conjunto))

#print(conjunto.intersection(conjunto2))
#print(conjunto.issubset((conjunto2)))#evalua si es un subconjunto y devuelve un valor de verdad
#print(conjunto.issuperset((conjunto2)))#evalua si es un superconjunto y devuelve un valor de verdad
print(conjunto)
conjunto.pop()#no se le pone i porque no tienen orden
#true y 1 son considerados el mismo valor
#false y o son considerados el mismo valor
#creacion llamando a un metodo contructor-programacion orientada a objetos : con set(("puedo","construir","un set")) e igualarlo a una variable
thisset = {"apple", "banana", True}

x = thisset.pop()

print(x) #removed item

print(thisset) #the set after removal


conjunto.remove("rojo")
print(conjunto.union(conjunto2))#union de dos conjuntos sin repetir elementos
