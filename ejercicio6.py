peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))
altura_cuadrado = altura * altura
imc = peso / altura_cuadrado
imc = (imc * 100) / 100
print(f"Peso ingresado: {peso} kg")
print(f"Altura ingresada: {altura} m")
print(f"Índice de Masa Corporal (IMC): {imc:.2f}")
if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc < 24.9:
    clasificacion = "Peso normal"
elif 25 <= imc < 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"
print(f"Clasificación del IMC: {clasificacion}")
