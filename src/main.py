# main.py

from estructuras import Entrenador
from pokemon import bulbasaur, charmander
from ataques import latigo_cepa, ascuas
from combate import turno

# Crear entrenadores
jugador = Entrenador("Humano", [bulbasaur])
ia = Entrenador("IA", [charmander])

# Turno de combate
turno(jugador.pokemon_activo(), ia.pokemon_activo(), latigo_cepa)
turno(ia.pokemon_activo(), jugador.pokemon_activo(), ascuas)
