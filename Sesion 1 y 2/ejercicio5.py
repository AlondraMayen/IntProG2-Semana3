segundos_totales = int(input("Ingrese la cantidad total de segundos: "))
horas = segundos_totales // 3600
resto = segundos_totales - (horas * 3600)
minutos = resto // 60
segundos = resto - (minutos * 60)
print(f"{horas} horas, {minutos} minutos, {segundos} segundos")