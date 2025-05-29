# ataques.py

from estructuras import Ataque

# Normal
placaje = Ataque("Placaje", "Normal", 30)
golpe_cuerpo = Ataque("Golpe Cuerpo", "Normal", 50)
giga_impacto = Ataque("Giga Impacto", "Normal", 90)

# Fuego
ascuas = Ataque("Ascuas", "Fuego", 30)
lanzallamas = Ataque("Lanzallamas", "Fuego", 60)
llamarada = Ataque("Llamarada", "Fuego", 90)

# Agua
burbuja = Ataque("Burbuja", "Agua", 20)
pistola_agua = Ataque("Pistola Agua", "Agua", 40)
hidrobomba = Ataque("Hidrobomba", "Agua", 70)

# Planta
latigo_cepa = Ataque("Látigo Cepa", "Planta", 30)
hoja_afilada = Ataque("Hoja Afilada", "Planta", 40)
rayo_solar = Ataque("Rayo Solar", "Planta", 70)

# Eléctrico
impactrueno = Ataque("Impactrueno", "Eléctrico", 30)
chispa = Ataque("Chispa", "Eléctrico", 40)
trueno = Ataque("Trueno", "Eléctrico", 70)

# Hielo
nieve_polvo = Ataque("Nieve Polvo", "Hielo", 30)
rayo_hielo = Ataque("Rayo Hielo", "Hielo", 40)
ventisca = Ataque("Ventisca", "Hielo", 70)

# Lucha
golpe_karate = Ataque("Golpe Karate", "Lucha", 30)
ultrapuño = Ataque("Ultrapuño", "Lucha", 40)
abocajarro = Ataque("Abocajarro", "Lucha", 70)

# Veneno
picotazo_venenoso = Ataque("Picotazo Venenoso", "Veneno", 30)
acido = Ataque("Ácido", "Veneno", 40)
bomba_lodo = Ataque("Bomba Lodo", "Veneno", 70)

# Tierra
bofeton_lodo = Ataque("Bofetón Lodo", "Tierra", 30)
excavar = Ataque("Excavar", "Tierra", 40)
terremoto = Ataque("Terremoto", "Tierra", 70)

# Volador
ataque_ala = Ataque("Ataque Ala", "Volador", 30)
tornado = Ataque("Tornado", "Volador", 40)
pajaro_osado = Ataque("Pájaro Osado", "Volador", 70)

# Psíquico
confusion = Ataque("Confusión", "Psíquico", 30)
psicoonda = Ataque("Psicoonda", "Psíquico", 50)
psiquico = Ataque("Psíquico", "Psíquico", 80)

# Bicho
picadura = Ataque("Picadura", "Bicho", 20)
tijera_x = Ataque("Tijera X", "Bicho", 50)
ida_y_vuelta = Ataque("Ida y Vuelta", "Bicho", 80)

# Roca
lanzarrocas = Ataque("Lanzarrocas", "Roca", 40)
avalancha = Ataque("Avalancha", "Roca", 60)
roca_afilada = Ataque("Roca Afilada", "Roca", 90)

# Fantasma
lenguetazo = Ataque("Lengüetazo", "Fantasma", 20)
sombra_vil = Ataque("Sombra Vil", "Fantasma", 50)
bola_sombra = Ataque("Bola Sombra", "Fantasma", 80)

# Dragón
dragoaliento = Ataque("Dragoaliento", "Dragón", 10)
pulso_dragon = Ataque("Pulso Dragón", "Dragón", 50)
cometa_draco = Ataque("Cometa Draco", "Dragón", 100)

# --- Diccionario por tipo ---
ATAQUES_POR_TIPO = {
    "Normal": [placaje, golpe_cuerpo, giga_impacto],
    "Fuego": [ascuas, lanzallamas, llamarada],
    "Agua": [burbuja, pistola_agua, hidrobomba],
    "Planta": [latigo_cepa, hoja_afilada, rayo_solar],
    "Eléctrico": [impactrueno, chispa, trueno],
    "Hielo": [nieve_polvo, rayo_hielo, ventisca],
    "Lucha": [golpe_karate, ultrapuño, abocajarro],
    "Veneno": [picotazo_venenoso, acido, bomba_lodo],
    "Tierra": [bofeton_lodo, excavar, terremoto],
    "Volador": [ataque_ala, tornado, pajaro_osado],
    "Psíquico": [confusion, psicoonda, psiquico],
    "Bicho": [picadura, tijera_x, ida_y_vuelta],
    "Roca": [lanzarrocas, avalancha, roca_afilada],
    "Fantasma": [lenguetazo, sombra_vil, bola_sombra],
    "Dragón": [dragoaliento, pulso_dragon, cometa_draco],
}

