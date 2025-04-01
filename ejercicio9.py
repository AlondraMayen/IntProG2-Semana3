duracion_pelicula = int(input("Ingrese la duración de la película en minutos: "))
duracion_comerciales_previos = int(input("Ingrese la duración de los comerciales previos en minutos: "))
cantidad_pausas = int(input("Ingrese la cantidad de pausas comerciales durante la película: "))
duracion_pausa = int(input("Ingrese la duración de cada pausa comercial en minutos: "))
comerciales_durante_pelicula = cantidad_pausas * duracion_pausa
duracion_total = duracion_pelicula + duracion_comerciales_previos + comerciales_durante_pelicula
print(f"Duración original de la película: {duracion_pelicula} minutos")
print(f"Duración total de los comerciales: {duracion_comerciales_previos + comerciales_durante_pelicula} minutos")
print(f"Duración total de la función: {duracion_total} minutos")