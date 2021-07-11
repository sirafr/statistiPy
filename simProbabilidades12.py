import random

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro1 = random.choice([1, 2, 3, 4, 5, 6])
        tiro2 = random.choice([1,2,3,4,5,6])

        resultado = tiro1+tiro2

        secuencia_de_tiros.append(resultado)

    return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        resultado = tirar_dado(numero_de_tiros)
        tiros.append(resultado)

    tiros_con_6 = 0
    for tiro in tiros:
        if 12 in tiro:
            tiros_con_6 += 1

    print(resultado)
    probabilidad_tiros_con_6 = tiros_con_6 / numero_de_intentos
    probabilidad_tiros_con_6S = 1 - probabilidad_tiros_con_6
    print(f'Probabilidad de obtener por lo menos un 1 en {numero_de_tiros} tiros = {probabilidad_tiros_con_6}')
    print(f'Probabilidad de no obtener por lo menos un 1 en {numero_de_tiros} tiros = {probabilidad_tiros_con_6S}')



if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantas tiros del dado: '))
    numero_de_intentos = int(input('Cuantas veces correra la simulacion: '))

    main(numero_de_tiros, numero_de_intentos)