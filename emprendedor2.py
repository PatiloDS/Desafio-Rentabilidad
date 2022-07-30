# Patricio Carrasco Zura

#formula Utilidades = P * U - GT
# P: precio suscripcion
# Un: Usuarios normales
# Up: usuarios premium 
# GT: Gastos totales
print("ingrese datos positivos si quieren un optimo resultado")
precio = float(input("ingrese el precio de la suscripcion: "))
usuarios = int(input("ingrese los usuarios normales: "))
usuarios_premium = int(input("ingrese los usuarios premium: "))
gasto = float(input("ingrese el gasto total ")) 

utilidades1= (precio*usuarios - gasto)
utilidades2= utilidades1+(utilidades1*0.5)
utt= utilidades1+utilidades2

print(f"las utilidades de usuarios normales son {utilidades1} y de los usuarios premium son {utilidades2} ")
print(f" y las utilidades totales son {utt} ")
