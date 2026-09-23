# dragones.py — Práctica 1.4: Reino de Dragones
# Completa los huecos marcados con ___ y ...
import random
import ___


def mostrar_introduccion():
    print('''Estás en una tierra llena de dragones. Frente a ti
hay dos cuevas. En una de ellas, el dragón es generoso y amigable
y compartirá su tesoro contigo. El otro dragón es codicioso
y está hambriento, y te devorará inmediatamente.''')
    print()


def elegir_cueva():
    cueva = ''
    while cueva != '1' ___ cueva != '2':
        print('¿A qué cueva quieres entrar? (1 o 2)')
        cueva = input()

    ___ cueva


def explorar_cueva(cueva_elegida):
    print('Te aproximas a la cueva...')
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.___(2)
    print('¡Un gran dragón aparece súbitamente frente a ti! Abre sus fauces y...')
    print()
    time.sleep(2)

    cueva_amigable = random.randint(1, 2)

    if cueva_elegida == ___(cueva_amigable):
        print('¡Te regala su tesoro!')
    else:
        ...


jugar_de_nuevo = 'sí'
while jugar_de_nuevo == 'sí' ___ jugar_de_nuevo == 's':
    mostrar_introduccion()
    numero_de_cueva = ___()
    explorar_cueva(___)

    print('¿Quieres jugar de nuevo? (sí o no)')
    jugar_de_nuevo = input()
