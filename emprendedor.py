#Pratricio Carrasco Zura

#formula Utilidades = P * U - GT
# P: precio suscripcion
# U: Numero usuarios
# GT: Gastos totales

usuarios = int(input("ingrese la cantidad de usuarios: "))
u= usuarios
precio = float(input("ingrese el precio de suscripcion: "))
p=precio
gastos = float(input("ingrese el gasto total: "))
gt= gastos

utilidades = (p*u-gt)
print(f"las utilidades son: {utilidades}")
