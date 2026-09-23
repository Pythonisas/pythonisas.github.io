# adivina_el_numero.py — Práctica 1.2: La esfera adivinatoria
# Completa los huecos marcados con ___ y ...
import ___

intentos_realizados = 0

print('¡Hola! ¿Cómo te llamas?')
mi_nombre = ___()

numero_secreto = random.___(1, 20)
print('Bueno, ' + mi_nombre + ', estoy pensando en un número entre 1 y 20.')

while intentos_realizados < ___:
    print('Intenta adivinar.')
    estimacion = input()
    estimacion = ___(estimacion)   # ¿Por qué hace falta esta línea?

    intentos_realizados = intentos_realizados + 1

    if estimacion < numero_secreto:
        print('Tu estimación es muy baja.')

    if estimacion ___ numero_secreto:
        print('Tu estimación es muy alta.')

    if estimacion == numero_secreto:
        ___

if estimacion == numero_secreto:
    intentos_realizados = ___(intentos_realizados)
    print('¡Buen trabajo, ' + mi_nombre + '! Has adivinado mi número en ' +
          intentos_realizados + ' intentos.')

if estimacion ___ numero_secreto:
    ...   # Muestra cuál era el número secreto
