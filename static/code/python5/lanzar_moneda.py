# lanzar_moneda.py — Práctica 1.5: puntos de interrupción
import random

print('Lanzaré una moneda 1000 veces. ¿Cuántas veces saldrá cara? (Pulsa Enter para empezar)')
input()
lanzamientos = 0
caras = 0
while lanzamientos < 1000:
    if random.randint(0, 1) == 1:
        caras = caras + 1
    lanzamientos = lanzamientos + 1

    if lanzamientos == 900:
        print('900 lanzamientos y ha salido cara ' + str(caras) + ' veces.')
    if lanzamientos == 100:
        print('En 100 lanzamientos, ha salido cara ' + str(caras) + ' veces.')
    if lanzamientos == 500:
        print('A mitad de camino, ha salido cara ' + str(caras) + ' veces.')

print()
print('De 1000 lanzamientos, ha salido cara ' + str(caras) + ' veces.')
print('¿Te has acercado?')
