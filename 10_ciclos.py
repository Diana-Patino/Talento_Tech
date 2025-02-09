"""
i = 1
while i <= 10:
    print(i)
    i += 1

numero = int(input("Dame un numeo :"))

if numero < 0:
    print("Ingresa un numero positivo")
else: 
    i = 0
    while i >= 0 and i < 10:
    #print(f"la tabla de multiplicar seria : {numero}  *  {i} =  {numero * i}")
        print("la tabla de multiplicar seria :", numero , "*" , i, "=" , numero * i)
        i += 1


i = 1
listadenume= []
while i <= 10:
    solicitud = int(input("dame un numero:"))
    listadenume.append(solicitud)
    i += 1
    
print(listadenume)
sumatoria = sum(listadenume)
print(sumatoria)
   
   


i = 1
while i < 6:
  print(i)
  if i == 3:
    break # rompre el codigo y sale de la caja
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #se salta una vuelta del ciclo segun la condicion que yo ponga
  print(i)
  """