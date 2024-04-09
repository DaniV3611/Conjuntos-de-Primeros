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

	simbolos_no_terminales = []
	reglas = []

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
			# Si el simbolo no terminal no existe, se crea
			if parte_izquierda[0] not in simbolos_no_terminales:
				simbolos_no_terminales.append(parte_izquierda[0])
			# Se guarda la regla actual
			# Tupla: 
			# * 0: Simbolo no terminal de la regla
			# * 1: Arreglo con los simbolos terminales o no terminales
			reglas.append((parte_izquierda[0], parte_derecha))

	return simbolos_no_terminales, reglas


archivo = leerArchivo()

no_terminales, reglas = leerGramatica(archivo)

print('Reglas: ')
print(reglas)
