# 16. Simulacion de barajas

import random
import collections

PALOS = ['espada','corazon','rombo','trebol']
VALORES = ['as','2','3','4','5','6','7','8','9','10','jota','reina','rey']

def crear_baraja ():
	barajas = []
	for palo in PALOS:
		for valor in VALORES:
			barajas.append((palo,valor))

	return barajas

def obtener_mano(barajas,tamano_mano):
	mano = random.sample(barajas,tamano_mano)

	return mano

def main(tamano_mano,intentos):
	barajas = crear_baraja()

	manos = []

	for _ in range(intentos):
		mano = obtener_mano(barajas,tamano_mano)
		manos.append(mano)


	pares = 0
	escalera26=0

	for mano in manos:
		valores = []

		for carta in mano:
			valores.append(carta[1])

		print(valores)

		counter = dict(collections.Counter(valores))

		for val1 in valores:
			if '2' in valores and '3' in valores  and '4' in valores  and '5' in valores  and '6':
				escalera26 +=1
			elif '3' in valores 

		for val in counter.values():
			if val == 2:
				pares += 1
				break

	probabilidad_par = pares/intentos
	probabilidad_26 = escalera26/intentos

	print(f'La probabilidad de obtener un par en una mano de {tamano_mano} es {probabilidad_par}')
	print(f'La probabilidad de obtener una escalera 2-6 de {tamano_mano} es {probabilidad_26}')
	print(counter)
	print(valores)


if __name__ == '__main__':
	tamano_mano = int(input('De cuantas barajas sera la mano: '))
	intentos=int(input('Cuantos intentos? '))


	main(tamano_mano,intentos)
