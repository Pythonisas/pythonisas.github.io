# ahorcado.py — Práctica 1.6: El Ahorcado
# Completa los huecos marcados con ___ y ...
import random

IMAGENES_AHORCADO = [r'''
  +---+
      |
      |
      |
     ===''', r'''
  +---+
  O   |
      |
      |
     ===''', r'''
  +---+
  O   |
  |   |
      |
     ===''', r'''
  +---+
  O   |
 /|   |
      |
     ===''', r'''
  +---+
  O   |
 /|\  |
      |
     ===''', r'''
  +---+
  O   |
 /|\  |
 /    |
     ===''', r'''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

PALABRAS = ('hormiga babuino tejon murcielago oso castor camello gato cobra '
            'coyote cuervo ciervo perro burro pato aguila zorro rana cabra '
            'ganso halcon leon lagarto llama topo mono raton mula nutria buho '
            'panda loro paloma piton conejo rata salmon foca tiburon oveja '
            'mofeta serpiente cisne tigre sapo trucha pavo tortuga ballena '
            'lobo cebra').___()


def obtener_palabra_al_azar(lista_de_palabras):
    # Devuelve una palabra al azar de la lista.
    indice = random.randint(0, ___(lista_de_palabras) - 1)
    return lista_de_palabras[___]


def mostrar_tablero(letras_incorrectas, letras_correctas, palabra_secreta):
    print(IMAGENES_AHORCADO[len(letras_incorrectas)])
    print()

    print('Letras incorrectas:', end=' ')
    for letra in ___:
        print(letra, end=' ')
    print()

    espacios = '_' * len(palabra_secreta)

    # Sustituye cada '_' por la letra acertada (¡cortes!)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] in letras_correctas:
            espacios = espacios[:i] + palabra_secreta[i] + espacios[___:]

    # Muestra la palabra con un espacio entre letras
    for letra in espacios:
        print(letra, end=' ')
    print()


def obtener_intento(letras_probadas):
    # Devuelve la letra introducida. Comprueba que sea UNA letra nueva.
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.___()
        if len(intento) != 1:
            print('Por favor, introduce una sola letra.')
        ___ intento in letras_probadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor, introduce una LETRA.')
        else:
            return ___


def jugar_de_nuevo():
    # Devuelve True si quiere volver a jugar y False si no.
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith(___)


print('A H O R C A D O')
letras_incorrectas = ''
letras_correctas = ''
palabra_secreta = obtener_palabra_al_azar(PALABRAS)
juego_terminado = False

while True:
    mostrar_tablero(letras_incorrectas, letras_correctas, palabra_secreta)

    intento = obtener_intento(letras_incorrectas + letras_correctas)

    if intento in palabra_secreta:
        letras_correctas = letras_correctas + intento

        # ¿Ha encontrado todas las letras?
        encontradas_todas = True
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] not in letras_correctas:
                encontradas_todas = ___
                break
        if encontradas_todas:
            print(f'¡Sí! La palabra secreta es "{palabra_secreta}". ¡Has ganado!')
            juego_terminado = True
    else:
        letras_incorrectas = letras_incorrectas + intento

        # ¿Se ha quedado sin intentos?
        if len(letras_incorrectas) == len(IMAGENES_AHORCADO) - 1:
            mostrar_tablero(letras_incorrectas, letras_correctas, palabra_secreta)
            print(f'¡Te has quedado sin intentos! La palabra era "{palabra_secreta}".')
            juego_terminado = ___

    if juego_terminado:
        if jugar_de_nuevo():
            ...   # Reinicia las letras y elige otra palabra secreta
        else:
            ___
