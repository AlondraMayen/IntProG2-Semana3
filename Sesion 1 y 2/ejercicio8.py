dolares = float(input("Ingrese la cantidad en dólares: "))
tasa_euro = 0.92  
tasa_libra = 0.78  
tasa_yen = 150.25  
euros = dolares * tasa_euro
libras = dolares * tasa_libra
yenes = dolares * tasa_yen
print(f"Cantidad en dólares: ${dolares:.2f}")
print(f"Equivalente en euros: €{euros:.2f}")
print(f"Equivalente en libras: £{libras:.2f}")
print(f"Equivalente en yenes: ¥{yenes:.2f}")