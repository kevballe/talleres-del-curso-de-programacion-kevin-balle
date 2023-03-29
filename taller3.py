#Crear un bucle que cuente todos los números pares hasta el 100 con el siclo for

for a in range(0,101,2):
    print(a)

#tabla de multiplicar

num = int(input("número a multiplicar: "))
for n in range(11):
    print(n,"X",num,"=",num*n)

#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad). ciclo for

edad= int(input("cuantos años tiene: "))
for e in range(1,edad+1,1):
    print(e)

#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

entero= int(input("escriba un numero entero mayor a 0: "))
resultado=""
for i in range(1,entero,1):
    if (i % 2!=0):
        resultado+=str(i)+","

print(resultado)
        


#Encuentra la suma de todos los números pares del 1 al 100 ciclo for

acu=0
for c in range(0,100,1):
    acu=acu+c
print(f"total de la suma de los numeros del 1 al 100 es={acu}")





