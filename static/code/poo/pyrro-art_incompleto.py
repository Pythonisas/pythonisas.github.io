#!/usr/bin/env python3
# pyrro-art.py — clase Pyrro con pyrro_dice() como método

import ___
import ___

# --- núcleo Funcional (reusable!) ---

def hacer_viñeta(text, width=40):
    lines = textwrap.wrap(text, width)
    max_len = max(len(l) for l in lines)
    border = "+" + "-" * (max_len + 2) + "+"
    body = "\n".join(f"| {l:<{max_len}} |" for l in lines)
    return f"{border}\n{body}\n{border}"

# --- Estilos de arte ASCII ---

PERROS = {
    "labrador": r"""
        \   / \__
         \ /  o  \
          /   (____)
         /___/  U
""",
    "___": r"""
        \   (  )
         \ (oo)
          /||\\
         (_||_)
          ^  ^
""",
    "___": r"""
        \  __  ____  __
         \/  \/    \/  \
         ( o            )--
          \____________/
""",
    "___": r"""
        \    / \
         \  (o o)
          \ / V \     guau. mucho perro.
           |  |  |    muy ascii.
           (__)__)
""",
}

# --- Clase Pyrro con pyrro_dice() como método ---

class ___:
    def __init__(self, name, edad, raza="labrador"):
        self.___ = name
        self.___ = edad
        self.___ = raza if raza in PERROS else "labrador"

    def sentarse(___):
        print(f"{self.name} ahora se sienta.")

    def dar_la_vuelta(self):
        print(f"{___.name} se da la vuelta!")

    def pyrro_dice(self, message=None):
        msg = message or f"Hola! Soy {self.___}, tengo {self.___} años. Guauu!"
        print(hacer_viñeta(___))
        print(PERROS[self.___])

    def arte_aleatorio(self, message=None):
        """Elige un arte de raza al azar."""
        self.raza = random.___(list(PERROS.___()))
        self.___(message)


# --- demo principal ---

if __name__ == "__main__":
    willie = ___("Willie", 6, "labrador")
    lucy   = ___("Lucy",   3, "shiba")
    rex    = ___("Rex",    5, "salchicha")

    willie.pyrro_dice("Creo que tengo pulgas. Guauauuu.")
    lucy.___(  "Me meo... donde lo hago, que no me vean?")
    rex.pyrro_dice("puedo ser alargado, pero mi código fuente no lo es.")

    print("--- Arte aleatorio ---")
    Pyrro("Buddy", 2).___(  "Raza sorpresa!")
