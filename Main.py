import sys

def leerArchivo():
	#Lee un archivo de python
	if len(sys.argv) != 2:
		print('Uso: python3 Main.py <archivo.txt>')
		sys.exit(0)
	
	#Obtener el nombre del archivo del primer argumento
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

# Calcula los primeros de una regla especifica
def calcularPrimero(simbolo_no_terminal, regla, reglas):

	primeros = []

	# Si la regla esta vacia
	if len(regla) == 0:
		primeros.append('/epsilon')
		return primeros

	# Se analiza el primer simbolo de la regla
	
	# Si el primer simbolo es terminal
	if regla[0] not in reglas:
		primeros.append(regla[0])
		return primeros
	
	# Si el primer simbolo es NO terminal
 
	# Guardar los no_terminales encontrados
	primeros_no_terminales = []
	
	# Se busca si este tiene mas simbolos NO terminales detras
	for simbolo in regla:
		if simbolo in reglas:
			# Si el no_terminal es el simbolo del que se esta calculando se ignora
			if simbolo != simbolo_no_terminal:
				temp = []
				# Se recorre cada regla del no_terminal para buscar sus primeros
				for regla_no_terminal in reglas[simbolo]:
					temp.append(calcularPrimero(simbolo, regla_no_terminal, reglas))

				# Se guardan los primeros encontrados
				lista = []
				for encontrado in temp:
					for simb in encontrado:
						# Se eliminan los repetidos
						if simb not in lista:
							lista.append(simb)

				primeros_no_terminales.append(lista)
		else:
			break

	# Se guardan los primeros encontrados en los primeros que se estan calculando
	agregar_vacio = True

	for primeros_encontrados in primeros_no_terminales:

		# Si algun conjunto no contiene vacio, este no se agregara
		if '/epsilon' not in primeros_encontrados:
			agregar_vacio = False

		for simbol in primeros_encontrados:
			if simbol not in primeros and simbol != '/epsilon':
				primeros.append(simbol)
		
	if agregar_vacio:
		primeros.append('/epsilon')
	
	return primeros

def calcularPrimeros(reglas):

	conjunto_primeros = {}
	conjunto_primeros_reglas = []

	for no_terminal in list(reglas.keys()):
		temp = []
		for regla in reglas[no_terminal]:
			primeros = calcularPrimero(no_terminal, regla, reglas)
			conjunto_primeros_reglas.append(primeros)
			temp.append(primeros)

		lista = []
		for elemento in temp:
			for simbol in elemento:
				if simbol not in lista:
					lista.append(simbol)

		conjunto_primeros[no_terminal] = lista

	return conjunto_primeros, conjunto_primeros_reglas

def imprimir(conjunto):
	for no_terminal, primeros in conjunto.items():
		print(f"Primeros de {no_terminal}")
		print(primeros)

archivo = leerArchivo()

reglas = leerGramatica(archivo)

primeros, conjunto_primeros_reglas = calcularPrimeros(reglas)
imprimir(primeros)
