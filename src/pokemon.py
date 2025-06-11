from estructuras import Pokemon
from ataques import *


#sets basicos
#set 1
bulbasaur = Pokemon("Bulbasaur", "Planta", 170, [latigo_cepa, placaje,picotazo_venenoso])
charmander = Pokemon("Charmander", "Fuego", 120, [ascuas, placaje,ataque_ala])
squirtle = Pokemon("Squirtle", "Agua", 150, [pistola_agua, placaje,golpe_karate])
pikachu = Pokemon("Pikachu", "Eléctrico", 100, [impactrueno, placaje, confusion])

#set 2
voltorb = Pokemon("Voltorb", "Eléctrico", 120, [impactrueno, placaje, ascuas])
seel = Pokemon("Seel", "Hielo", 140, [nieve_polvo, placaje, burbuja])
pidgey = Pokemon("Pidgey", "Volador", 120, [ataque_ala, placaje, bofeton_lodo])
Abra = Pokemon("Abra", "Psíquico", 110, [confusion, placaje, lanzarrocas])

#set 3
jigglypuff = Pokemon("Jigglypuff", "Normal", 160, [placaje, confusion, bofeton_lodo])
geodude = Pokemon("Geodude", "Roca", 160, [lanzarrocas, placaje, golpe_karate])
weedle = Pokemon("Weedle", "Bicho", 100, [picadura, placaje, picotazo_venenoso])
ekans = Pokemon("Ekans", "Veneno", 120, [picotazo_venenoso, placaje, ascuas])

#sets medios
#set 1
jinx = Pokemon("Jynx", "Hielo", 200, [rayo_hielo, golpe_cuerpo, sombra_vil])
magmar = Pokemon("Magmar", "Fuego", 210, [lanzallamas, golpe_cuerpo, bola_sombra])
electabuzz = Pokemon("Electabuzz", "Eléctrico", 200, [chispa, golpe_cuerpo, pulso_dragon])
scyther = Pokemon("Scyther", "Bicho", 190, [tijera_x, golpe_cuerpo, tornado])

#set 2
omanyte = Pokemon("Omanyte", "Roca", 220, [pistola_agua, rayo_hielo, avalancha])
kabutops = Pokemon("Kabutops", "Roca", 190, [lanzarrocas, pistola_agua, tijera_x])
aerodactyl = Pokemon("Aerodactyl", "Roca", 190, [avalancha, tornado, excavar])
snorlax = Pokemon("Snorlax", "Normal", 240, [golpe_cuerpo, excavar, ultrapuño])

#set 3
chansey = Pokemon("Chansey", "Normal", 250, [psicoonda, golpe_cuerpo, pulso_dragon])
gyarados = Pokemon("Gyarados", "Agua", 210, [pistola_agua, golpe_cuerpo, tornado])
jolteon = Pokemon("Jolteon", "Eléctrico", 200, [tijera_x, golpe_cuerpo, chispa])
arcanine = Pokemon("Arcanine", "Fuego", 210, [lanzallamas, golpe_cuerpo, excavar])

#sets avanzados
#set 1
articuno = Pokemon("Articuno", "Hielo", 350, [hidrobomba, ventisca, pajaro_osado])
zapdos = Pokemon("Zapdos", "Eléctrico", 400, [trueno, llamarada, pajaro_osado])
moltres = Pokemon("Moltres", "Fuego", 390, [llamarada, pulso_dragon, pajaro_osado])
mewtwo = Pokemon("Mewtwo", "Psíquico", 400, [psiquico, abocajarro, bola_sombra])
#set 2
gengar = Pokemon("Gengar", "Fantasma", 380, [bomba_lodo, bola_sombra, trueno])
alakazam = Pokemon("Alakazam", "Psíquico", 360, [psiquico, llamarada, rayo_solar])
golem = Pokemon("Golem", "Roca", 410, [roca_afilada, terremoto, abocajarro])
machamp = Pokemon("Machamp", "Lucha", 390, [trueno, abocajarro, roca_afilada])
#set 3
dragonite = Pokemon("Dragonite", "Dragón", 400, [trueno, pajaro_osado, cometa_draco])
venasaur = Pokemon("Venusaur", "Planta", 410, [rayo_solar, bomba_lodo, terremoto])
charizard = Pokemon("Charizard", "Fuego", 380, [llamarada, pajaro_osado, cometa_draco])
blastoise = Pokemon("Blastoise", "Agua", 400, [hidrobomba, ventisca, giga_impacto])

POKEMONES = {
    "bulbasaur": bulbasaur,
    "charmander": charmander,
    "squirtle": squirtle,
    "pikachu": pikachu,
    "voltorb": voltorb,
    "seel": seel,
    "pidgey": pidgey,
    "abra": Abra,
    "jigglypuff": jigglypuff,
    "geodude": geodude,
    "weedle": weedle,
    "ekans": ekans,
    "jinx": jinx,
    "magmar": magmar,
    "electabuzz": electabuzz,
    "scyther": scyther,
    "omanyte": omanyte,
    "kabutops": kabutops,
    "aerodactyl": aerodactyl,
    "snorlax": snorlax,
    "chansey": chansey,
    "gyarados": gyarados,
    "jolteon": jolteon,
    "arcanine": arcanine,
    "articuno": articuno,
    "zapdos": zapdos,
    "moltres": moltres,
    "mewtwo": mewtwo,
    "gengar": gengar,
    "alakazam": alakazam,
    "golem": golem,
    "machamp": machamp,
    "dragonite": dragonite,
    "venasaur": venasaur,
    "charizard": charizard,
    "blastoise": blastoise
    
    
}

__all__ = ["POKEMONES"]
