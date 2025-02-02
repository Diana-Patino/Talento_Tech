# Esta es mi primera clase de programacion basico, talento tech
print("Hola Dianita bonita")
print("¿como estas el dia de hoy?")

#Tipos de daltos
 
x = 5 #int
y = 5.5 #float
z = "dianita" #str
w = True #bool

print(x)
print(y)
print(z)
print(w)

print(type(x))
print(type(y))
print(type(z))
print(type(w))

#Operadores
a=4
b=4
c = a + b 
print(c)

a ="hola" 
b ="Dianita bonita"
c = a + b 
print(c)


a = int(input("dame un numero"))
b = int(input("dame otro numero"))
c = a + b 
d = a - b
e = a/b
f = a//b
g = a**b
h = a*b
i = a%b
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

print("si tu sumas ",a,"mas",b,"el resultado es", c)
print("si tu restas ",a,"menos",b,"el resultado es", d)
print("si tu divides ",a,"dividido",b,"el resultado es", e)
print("si tu multiplicas ",a,"por",b,"el resultado es", h)
print("si tu elevas ",a,"a la exponencia",b,"el resultado es", c)
print("si buscas el residuo de la division de ", a , "dividido entre", b, "el residuo es",i)

print("la suma de los numeros es :", int(a + b))

print("esta es una practica", y, w)


print("Buen dia, soy Mario y voy a ayudarte con tu facturacion")
print(input("Primero que todo dime como te llaman :"))

uno = int(input("cuanto cuesta tu primer articulo"))
dos = int(input("cuanto cuesta tu segundo articulo"))
tres = int(input("cuanto cuesta tu tercer articulo"))
costo = float(uno+dos+tres)
print("el total de tu factura es:", costo )

cobre = int(input("con cuanto vas a pagar?"))

print("te debo devolver :",(cobre-costo) )


print("Hola, soy un codigo que se sabe las tablas de multiplicar, dame un reto!")
numero = int(input("¿de que numero quieres que te enseñe la tabla de miltiplicar?"))

a= numero * 1
b= numero * 2
c= numero * 3
d= numero * 4
e= numero * 5
f= numero * 6
g= numero * 7
h= numero * 8
i=numero*9
j=numero*10

print("esta es la tabla del :",numero,"empezamos", numero, "* 1:" ,a,"/",numero, "* 2:",b,"/",numero, "* 3:",c,"/",numero, "* 4:","/",d,numero, "* 5:",e,"/",numero, "* 6:",f,"/",numero, "* 7:",g,"/",numero, "* 8:",h,"/",numero, "* 9:",i,"/",numero, "* 10:",j,"/")



#Operadores de comparacion

print("esta es la verificacion legal requerida para acceder")
x = (input("cual es tu edad"))

b = x >= 18

