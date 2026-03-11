#!/usr/bin/env python3
# pyrro-dice.py — KISS + estilo funcional

import ___
import ___

PYRRO = r"""
        \  / \__
         \/  o  \
         /   (___)  GUAUU!
        /_____/
"""

def hacer_viñeta(___, width=40):
    lines = textwrap.wrap(___, width)
    max_len = max(len(l) for l in lines)
    border = "+" + "-" * (max_len + 2) + "+"
    body = "\n".join(f"| {l:<{max_len}} |" for l in lines)
    return f"{border}\n{body}\n{border}"

def pyrro_dice(___):
    print(hacer_viñeta(___))
    print(___)

if __name__ == "___":
    msg = " ".join(sys.argv[1:]) or "GUAU! Soy un buen perro."
    ___(msg)
