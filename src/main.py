# main.py

from ataques import *
from combate import turno
from estructuras import Entrenador
from pokemon import (
    bulbasaur, charmander, squirtle, pikachu,
    voltorb, seel, pidgey, Abra,
    jigglypuff, geodude, weedle, ekans,
    jinx, magmar, electabuzz, scyther,
    omanyte, kabutops, aerodactyl, snorlax,
    chansey, gyarados, jolteon, arcanine,
    articuno, zapdos, moltres, mewtwo,
    gengar, alakazam, golem, machamp,
    dragonite, venasaur, charizard, blastoise
)

# Entrenadores de sets básicos
entrenador_basico_1 = Entrenador("Ash Básico", [bulbasaur, charmander, squirtle, pikachu])
entrenador_basico_2 = Entrenador("Surge Básico", [voltorb, seel, pidgey, Abra])
entrenador_basico_3 = Entrenador("Jessie Básico", [jigglypuff, geodude, weedle, ekans])

# Entrenadores de sets medios
entrenador_medio_1 = Entrenador("Lorelei Medio", [jinx, magmar, electabuzz, scyther])
entrenador_medio_2 = Entrenador("Brock Medio", [omanyte, kabutops, aerodactyl, snorlax])
entrenador_medio_3 = Entrenador("Erika Medio", [chansey, gyarados, jolteon, arcanine])

# Entrenadores de sets avanzados
entrenador_avanzado_1 = Entrenador("Elite 4 - Articuno", [articuno, zapdos, moltres, mewtwo])
entrenador_avanzado_2 = Entrenador("Elite 4 - Fantasma", [gengar, alakazam, golem, machamp])
entrenador_avanzado_3 = Entrenador("Elite 4 - Final", [dragonite, venasaur, charizard, blastoise])


# Turno de combate
turno(jugador.pokemon_activo(), ia.pokemon_activo(), latigo_cepa)
turno(ia.pokemon_activo(), jugador.pokemon_activo(), ascuas)
