# Patricio Carrasco Zura

#formula Utilidades = P * U - GT
# P: precio suscripcion
# Un: Usuarios normales
# Up: usuarios premium 
# GT: Gastos totales
print("ingrese datos positivos si quieren un optimo resultado")
precio = float(input("ingrese el precio de la suscripcion: "))
usuarios = int(input("ingrese los usuarios normales: "))
gasto = float(input("ingrese el gasto total ")) 
util1 = float(input("ingrese las utilidades del año pasado: "))

utilidades1= (precio*usuarios - gasto)
utt = utilidades1/util1

print(f"las utilidades actuales son: {utilidades1}")
print(f"la razon entre las utilidades del año pasao y año actual es: {utt}")