#Leer x cantidad del producto comprado a x precio
#Implica el iva 15%
#Un descuento del 10%
#Mostrar el Total antes del IVA
#Monto del iva
#Monto de descuento
#Total a pagar
""""Se debe leer el nombre del cliente, nombre del producto y mostrar una factura """
print ("="*20)
print ("Sistema de Facturación")
print ("="*20)
print ("Ingresa los siguientes datos")
cliente = input("Nombre del cliente: ")
producto = input("Nombre del producto:")
precio = float(input("Precio del producto:"))
cantidad = float (input("Cantidad del producto:"))

total = precio * cantidad
iva = total * 0.15
descuento = total * 0.1

monto = total + iva - descuento

import os
press_key = input("Preciona una tecla para continuar...")
os.system("cls || clear")
print("+"*30)
print("Factura")
print("+"*30)
print (f"Cliente :{cliente}")
print(f"Productos \t Cantidad \t Precio \t Total")
print(f"{producto} {cantidad} {precio} {total}")
print(f"IVA: {iva}")
print(f"descuento: \t {descuento}")
print(f"Monto: {monto}")