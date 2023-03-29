nota1 = float(input("digite la calificacion 1: "))
nota2 = float(input("digite la calificacion 2: "))
nota3 = float(input("digite la calificacion 3: "))

prom = round((nota1 +nota2 + nota3)/3 ,2)

if prom < 3.0:
    estado = "reprobo"
else:
    estado ="aprobo"
    print(f"el promedio es={prom} y el estado es= {estado}")


num1=input("escriba el numero1: ")
num2=input("escriba el numero2: ")
if num1==num2:
    print("los numeros son iguales")
else:
    print("los numeros NO son iguales")

# > mayor que, < menor que, >= mayor o igual que, <= menor o igual que, == igual que, != diferente que,ambos debe ser iguales and, uno de los debe ser verdadero or, in texto inmerso en otro

usuario = input("digite su usuario: ")
usudb = "kevin1608"

if usuario == usudb:
  print("el usuario es correcto")
else:
  print("el usuario es incorrecto")

# condiciones para un objeto

num = int(input("digite el número: "))
if num > 30:
   print("el número es mayor a 30")
elif num > 20:
   print("el número es mayor a 20")
elif num > 10:
   print("el numero es mayor a 10")
else:
   print("no se cumple ninguna condición")

Edad = int(input("digite su edad: "))
if Edad >= 15 and Edad < 25:
   print("Apto para inscribirse")
else:
   print("No apto para la inscripcion")

   
