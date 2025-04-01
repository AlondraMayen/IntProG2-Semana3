import math
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))
area_base = math.pi * radio ** 2
volumen = area_base * altura
area_lateral = 2 * math.pi * radio * altura
area_superficial = area_lateral + 2 * area_base
print(f"Radio ingresado: {radio}")
print(f"Altura ingresada: {altura}")
print(f"Volumen del cilindro: {volumen:.2f}")
print(f"Área superficial del cilindro: {area_superficial:.2f}")