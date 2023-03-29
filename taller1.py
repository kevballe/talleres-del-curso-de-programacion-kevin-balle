N_identificación=input("digite su numero de indentificacion: ")
print(N_identificación)
Nombre="kevin"
apellidos="Ballesteros Carreño"
dirección=input("digite su direccion: ")
teléfono="3112078657"
Edad=int(input("digite su edad"))
estado_civil=(input("digite su estado civil: "))
n_hijos=int(input("ingrese el numero de hijos: "))
Estatura=input("ingrese su estatura: cm")
Fecha_de_contratación="06/06/2020"
sueldo_basico= float(input("ingrese su sueldo basico: "))
dias_laborados=int(input("ingrese los dias laborados: "))
print(N_identificación," \n",Nombre," ",apellidos," \n",dirección," \n",teléfono," \n",Edad," \n",estado_civil," \n",n_hijos," \n",Estatura," \n",Fecha_de_contratación," \n",sueldo_basico," \n",dias_laborados)

if Edad >= 55:
    bono= sueldo_basico * 0.05
    total = sueldo_basico + bono
    print("el bono de pension es =${:,.0f} y el salario a pagar es =${:,.0f}".format(bono , total))
else:
    print(f"No tiene bono, su salario es =${sueldo_basico:,.0f}")

if estado_civil == "casado" and n_hijos > 0:
  print("habilitado para viaje anual en diciembre")
else:
   print("no tiene opcion de viaje en diciembre")

if sueldo_basico >= 1000000 and sueldo_basico < 1500000:
  com2 = sueldo_basico * 0.2
  print(f"Tiene un bono de comisión del 2%: {com2:,.0f}")

if sueldo_basico >= 1500001 and sueldo_basico < 2000000:
  com5 = sueldo_basico * 0.5
  print(f"Tiene un bono de comisión del 5%: {com5:,.0f}")
  
if dias_laborados > 20 and sueldo_basico < 1000000:
  print("Aplica para bono de alimentación")
else:
   print("En esta oportunidad no aplicas para bono de alimentación")
   