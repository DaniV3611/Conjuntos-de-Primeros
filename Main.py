import sys

def leerArchivo():
	# Lee un archivo de python
	if len(sys.argv) != 2:
	    print("Uso: python3 Main.py <archivo.py>")
	    sys.exit(1)

	# Obtener el nombre del archivo del primer argumento
	python_file = sys.argv[1]

	archivo = []

	with open(python_file, 'r') as file:
		for linea in file:
			archivo.append(linea)

	return archivo

def leerGramatica (archivo):

	reglas = {}

	for linea in archivo:

		# Detectar el indicador

		indice_indicador = 0

		for i in range(0, len(linea)):

			if linea[i] == '-':
				if linea[i + 1] == '>':
					indice_indicador = i
					break
			else:
				continue

		parte_izquierda = linea[0: indice_indicador].split()
		parte_derecha = linea[(indice_indicador + 2): -1].split()

		# Si hay un simbolo no terminal
		if len(parte_izquierda) != 0:
			
			# Si la clave no existe en el diccionario se inicializa

			if parte_izquierda[0] not in reglas:
				reglas[parte_izquierda[0]] = []

			reglas[parte_izquierda[0]].append(parte_derecha)

	return reglas


archivo = leerArchivo()

reglas = leerGramatica(archivo)

print('Reglas: ')
print(reglas)
