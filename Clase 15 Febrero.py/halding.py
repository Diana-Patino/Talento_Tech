# open()
# "r" - Read
# "a" - Append
# "w" - Write
# "x" - Create

# "t" - Text 
# "b" - Binary


"""

f = open("demofile.txt")
f = open("demofile.txt", "rt")

Para abrir archivos

f = open("demofile.txt", "r")
print(f.read()) - imprime lo que leyo

f = open("demofile.txt", "r")
print(f.read(5)) - accede aun caracter especifico

accede a una linea de lectura

f = open("demofile.txt", "r")
print(f.readline())

para acceder a las dos primeras linea de lecturas llamo readline dos veces

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

para recorrer un archivo linea por linea 
f = open("demofile.txt", "r")
for x in f:
  print(x)

para cerrar el archivo

f = open("demofile.txt", "r")
print(f.readline())
f.close()

para agregar cosas al archivi 

"a" - Append  se agrega al final del archivo

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()


"w" - Write - sobre escribe lo existente
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())


"""