from estructuras import Pokemon
from ataques import *

#sets basicos
#set 1
bulbasaur = Pokemon("Bulbasaur", "Planta", 100, [latigo_cepa, placaje,picotazo_venenoso])
charmander = Pokemon("Charmander", "Fuego", 100, [ascuas, placaje,ataque_ala])
squirtle = Pokemon("Squirtle", "Agua", 100, [pistola_agua, placaje,golpe_karate])
pikachu = Pokemon("Pikachu", "Eléctrico", 100, [impactrueno, placaje, confusion])

#set 2
voltorb = Pokemon("Voltorb", "Eléctrico", 100, [impactrueno, placaje, ascuas])
seel = Pokemon("Seel", "Hielo", 100, [nieve_polvo, placaje, burbuja])
pidgey = Pokemon("Pidgey", "Volador", 100, [ataque_ala, placaje, bofeton_lodo])
Abra = Pokemon("Abra", "Psíquico", 100, [confusion, placaje, lanzarrocas])

#set 3
jigglypuff = Pokemon("Jigglypuff", "Normal", 100, [placaje, confusion, bofeton_lodo])
geodude = Pokemon("Geodude", "Roca", 100, [lanzarrocas, placaje, golpe_karate])
weedle = Pokemon("Weedle", "Bicho", 100, [picadura, placaje, picotazo_venenoso])
ekans = Pokemon("Ekans", "Veneno", 100, [picotazo_venenoso, placaje, ascuas])

#sets medios
#set 1
jinx = Pokemon("Jynx", "Hielo", 100, [rayo_hielo, golpe_cuerpo, sombra_vil])
magmar = Pokemon("Magmar", "Fuego", 100, [lanzallamas, golpe_cuerpo, bola_sombra])
electabuzz = Pokemon("Electabuzz", "Eléctrico", 100, [chispa, golpe_cuerpo, pulso_dragon])
scyther = Pokemon("Scyther", "Bicho", 100, [tijera_x, golpe_cuerpo, tornado])

#set 2
omanyte = Pokemon("Omanyte", "Roca", 100, [pistola_agua, rayo_hielo, avalancha])
kabutops = Pokemon("Kabutops", "Roca", 100, [lanzarrocas, pistola_agua, tijera_x])
aerodactyl = Pokemon("Aerodactyl", "Roca", 100, [avalancha, tornado, excavar])
snorlax = Pokemon("Snorlax", "Normal", 100, [golpe_cuerpo, excavar, ultrapuño])

#set 3
chansey = Pokemon("Chansey", "Normal", 100, [psicoonda, golpe_cuerpo, pulso_dragon])
gyarados = Pokemon("Gyarados", "Agua", 100, [pistola_agua, golpe_cuerpo, tornado])
jolteon = Pokemon("Jolteon", "Eléctrico", 100, [tijera_x, golpe_cuerpo, chispa])
arcanine = Pokemon("Arcanine", "Fuego", 100, [lanzallamas, golpe_cuerpo, excavar])

#sets avanzados
#set 1
articuno = Pokemon("Articuno", "Hielo", 100, [hidrobomba, ventisca, pajaro_osado])
zapdos = Pokemon("Zapdos", "Eléctrico", 100, [trueno, llamarada, pajaro_osado])
moltres = Pokemon("Moltres", "Fuego", 100, [llamarada, pulso_dragon, pajaro_osado])
mewtwo = Pokemon("Mewtwo", "Psíquico", 100, [psiquico, abocajarro, bola_sombra])
#set 2
gengar = Pokemon("Gengar", "Fantasma", 100, [bomba_lodo, bola_sombra, trueno])
alakazam = Pokemon("Alakazam", "Psíquico", 100, [psiquico, llamarada, rayo_solar])
golem = Pokemon("Golem", "Roca", 100, [roca_afilada, terremoto, abocajarro])
machamp = Pokemon("Machamp", "Lucha", 100, [trueno, abocajarro, roca_afilada])
#set 3
dragonite = Pokemon("Dragonite", "Dragón", 100, [trueno, pajaro_osado, cometa_draco])
venasaur = Pokemon("Venusaur", "Planta", 100, [rayo_solar, bomba_lodo, terremoto])
charizard = Pokemon("Charizard", "Fuego", 100, [llamarada, pajaro_osado, cometa_draco])
blastoise = Pokemon("Blastoise", "Agua", 100, [hidrobomba, ventisca, giga_impacto])

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

