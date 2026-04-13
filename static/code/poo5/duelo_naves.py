#!/usr/bin/env python3
import random
import time

class Nave:
    def __init__(self, nombre, escudo, combustible):
        self.nombre = nombre
        self.escudo = escudo
        self.combustible = combustible

    def estado_visual(self):
        barra = "█" * (self.escudo // 10)
        return f"[{barra:<10}] {self.escudo}%"

def iniciar_duelo():
    print("\n" + "!"*50)
    print("   ¡ALERTA DE COMBATE! NAVE PIRATA DETECTADA")
    print("!"*50)
    
    nombre_usuario = input("Capitán, nombre de su nave: ").upper()
    jugador = Nave(nombre_usuario, 100, 100)
    enemigo = Nave("CRUCERO PIRATA", 120, 999)

    while jugador.escudo > 0 and enemigo.escudo > 0:
        # Interfaz de combate
        print(f"\n🚀 {jugador.nombre}: {jugador.estado_visual()} | ⛽ Combustible: {jugador.combustible}%")
        print(f"🏴‍☠️ {enemigo.nombre}: {enemigo.estado_visual()}")
        print("-" * 50)
        
        print("¿ÓRDENES?")
        print("1. DISPARAR (-10 comb. | -20 daño)")
        print("2. MEGA-LÁSER (-30 comb. | -50 daño)")
        print("3. REPARAR (+25 escudo | -15 comb.)")
        print("4. ESQUIVAR (Evita el siguiente golpe | -10 comb.)")
        
        opcion = input("\nSeleccione (1-4): ").strip()

        esquivando = False

        if opcion == "1":
            if jugador.combustible >= 10:
                jugador.combustible -= 10
                daño = 20
                enemigo.escudo -= daño
                print(f"🎯 ¡Impacto! El pirata sufre -{daño} de daño.")
                # BONUS: Robar combustible
                if random.random() < 0.4:
                    robo = random.randint(5, 15)
                    jugador.combustible = min(100, jugador.combustible + robo)
                    print(f"📦 ¡Has succionado {robo}% de combustible del enemigo!")
            else: print("⚠️ ¡Sin energía para disparar!")
        
        elif opcion == "2":
            if jugador.combustible >= 30:
                jugador.combustible -= 30
                enemigo.escudo -= 50
                print("⚡ ¡BUM! La mega-carga sacude al crucero pirata.")
            else: print("⚠️ Energía insuficiente para el Mega-Láser.")
        
        elif opcion == "3":
            if jugador.combustible >= 15:
                jugador.combustible -= 15
                jugador.escudo = min(100, jugador.escudo + 25)
                print("🛠️  Reparando planchas de casco...")
            else: print("⚠️ No hay energía para reparaciones.")
        
        elif opcion == "4":
            if jugador.combustible >= 10:
                jugador.combustible -= 10
                esquivando = True
                print("✈️  Maniobra evasiva iniciada.")
            else: print("⚠️ Demasiado pesado para esquivar.")
        
        else:
            print("❌ ERROR DE SISTEMA: Orden no válida.")
            continue # Salta el turno del enemigo si te equivocas de tecla

        # Turno del Enemigo
        if enemigo.escudo > 0:
            time.sleep(1)
            if esquivando:
                print("\n💨 ¡El pirata dispara pero fallas por los pelos!")
            else:
                ataque_enemigo = random.randint(15, 25)
                jugador.escudo -= ataque_enemigo
                print(f"\n💥 ¡EL PIRATA RESPONDE! Te quita {ataque_enemigo}% de escudo.")

        # Verificar combustible crítico
        if jugador.combustible <= 0:
            print("\n🪫 COMBUSTIBLE AGOTADO. Te has quedado a la deriva...")
            jugador.escudo = 0

    # Resultado final
    if jugador.escudo > 0:
        print(f"\n🏆 ¡VICTORIA! El espacio vuelve a ser seguro para la {jugador.nombre}.")
    else:
        print("\n💀 DERROTA. Tu nave se ha convertido en chatarra espacial.")

if __name__ == "__main__":
    iniciar_duelo()