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

def calcularPrimero(simbolo_no_terminal, reglas):
	primeros = []
	# Se analiza el primer simbolo de cada una de las reglas
	for  regla in reglas.get(simbolo_no_terminal):

		# print(f"Regla: {regla}")
		
		# Si la regla es vacia
		if len(regla) == 0:
			if '/epsilon' not in primeros:
				primeros.append('/epsilon')
		# Si el simbolo es terminal
		elif regla[0] not in reglas:
			if regla[0] not in primeros:
				primeros.append(regla[0])
		else:
			if regla[0] != simbolo_no_terminal:
				for primero in calcularPrimero(regla[0], reglas):
					if primero == '/epsilon':
						if len(regla) == 1:
							if primero not in primeros:
								primeros.append(primero)
						else:
							continue
					if primero not in primeros:
						primeros.append(primero)

	return primeros

def calcularPrimeros(reglas):

	conjunto_primeros = {}

	for no_terminal in list(reglas.keys()):
		conjunto_primeros[no_terminal] = calcularPrimero(no_terminal, reglas)

	return conjunto_primeros

def imprimir(conjunto):
	for no_terminal, primeros in conjunto.items():
		print(f"Primeros de {no_terminal}")
		print(primeros)

archivo = leerArchivo()

reglas = leerGramatica(archivo)

primeros = calcularPrimeros(reglas)
imprimir(primeros)
