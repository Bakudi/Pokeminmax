# main.py

from ataques import *
from combate import turno
from estructuras import Entrenador
from pokemon import bulbasaur, charmander, squirtle, pikachu, voltorb, seel, pidgey, Abra
from minimax import elegir_mejor_ataque

# Crear entrenadores
jugador = Entrenador("Jugador", [bulbasaur])
ia = Entrenador("IA", [charmander])

# Asignar Pokémon activos
pokemon_jugador = jugador.pokemon_activo()
pokemon_ia = ia.pokemon_activo()

# Combate por turnos
print("\n--- ¡COMIENZA EL COMBATE! ---\n")
while True:
    # Mostrar estado
    print(f"{pokemon_jugador.nombre}: {pokemon_jugador.ps} PS")
    print(f"{pokemon_ia.nombre}: {pokemon_ia.ps} PS\n")

    # Verificar fin de combate
    if pokemon_jugador.ps <= 0:
        print("¡Tu Pokémon ha sido derrotado! La IA gana.")
        break
    elif pokemon_ia.ps <= 0:
        print("¡Has ganado el combate!")
        break

    # Turno del jugador
    print(f"\nTu turno. Elige un ataque para {pokemon_jugador.nombre}:")
    for i, ataque in enumerate(pokemon_jugador.ataques):
        print(f"{i+1}. {ataque}")

    while True:
        try:
            opcion = int(input("Número del ataque: ")) - 1
            if 0 <= opcion < len(pokemon_jugador.ataques):
                ataque_jugador = pokemon_jugador.ataques[opcion]
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Por favor ingresa un número.")

    turno(pokemon_jugador, pokemon_ia, ataque_jugador)

    # Verificar si IA fue derrotada
    if pokemon_ia.ps <= 0:
        print("¡Has ganado el combate!")
        break

    # Turno de la IA
    print("\nTurno de la IA:")
    ataque_ia = elegir_mejor_ataque(pokemon_ia, pokemon_jugador)
    print(f"La IA elige usar: {ataque_ia.nombre}\n")
    turno(pokemon_ia, pokemon_jugador, ataque_ia)

    # Verificar si jugador fue derrotado
    if pokemon_jugador.ps <= 0:
        print("¡Tu Pokémon ha sido derrotado! La IA gana.")
        break
