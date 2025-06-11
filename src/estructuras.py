from dataclasses import dataclass
from typing import List, Optional

# tabla de tipos

efectividad = {
    #tipo normal
    ("normal", "normal"): 1.0,
    ("normal", "fuego"): 0.5,
    ("normal", "agua"): 0.5,
    ("normal", "planta"): 0.5,
    ("normal", "fantasma"): 0.0,
    ("normal", "lucha"): 1.0,
    ("normal", "veneno"): 1.0,
    ("normal", "tierra"): 1.0,
    ("normal", "volador"): 1.0,
    ("normal", "psíquico"): 1.0,
    ("normal", "bicho"): 1.0,
    ("normal", "roca"): 0.5,
    ("normal", "dragón"): 1.0,
    ("normal", "hielo"): 1.0,
    ("normal", "eléctrico"): 1.0,
    
    #fuego
    ("fuego", "normal"): 1.0,
    ("fuego", "fuego"): 0.5,
    ("fuego", "agua"): 0.5,
    ("fuego", "planta"): 2.0,
    ("fuego", "fantasma"): 1.0,
    ("fuego", "lucha"): 1.0,
    ("fuego", "veneno"): 1.0,
    ("fuego", "tierra"): 1.0,
    ("fuego", "volador"): 1.0,
    ("fuego", "psíquico"): 1.0,
    ("fuego", "bicho"): 2.0,
    ("fuego", "roca"): 0.5,
    ("fuego", "dragón"): 0.5,
    ("fuego", "hielo"): 2.0,
    
    #agua
    ("agua", "normal"): 1.0,
    ("agua", "fuego"): 2.0,
    ("agua", "agua"): 0.5,
    ("agua", "planta"): 0.5,
    ("agua", "fantasma"): 1.0,
    ("agua", "lucha"): 1.0,
    ("agua", "veneno"): 1.0,
    ("agua", "tierra"): 2.0,
    ("agua", "volador"): 1.0,
    ("agua", "psíquico"): 1.0,
    ("agua", "bicho"): 1.0,
    ("agua", "roca"): 2.0,
    ("agua", "dragón"): 0.5,
    ("agua", "hielo"): 1.0,
    ("agua", "eléctrico"): 0.5,

    #planta
    ("planta", "normal"): 1.0,
    ("planta", "fuego"): 0.5,
    ("planta", "agua"): 2.0,
    ("planta", "planta"): 0.5,
    ("planta", "fantasma"): 1.0,
    ("planta", "lucha"): 1.0,
    ("planta", "veneno"): 0.5,
    ("planta", "tierra"): 2.0,
    ("planta", "volador"): 0.5,
    ("planta", "psíquico"): 1.0,
    ("planta", "bicho"): 0.5,
    ("planta", "roca"): 2.0,
    ("planta", "dragón"): 0.5,
    ("planta", "hielo"): 1.0,
    ("planta", "eléctrico"): 1.0,
    
    #electrico
    ("eléctrico", "normal"): 1.0,
    ("eléctrico", "fuego"): 1.0,
    ("eléctrico", "agua"): 2.0,
    ("eléctrico", "planta"): 0.5,
    ("eléctrico", "fantasma"): 1.0,
    ("eléctrico", "lucha"): 1.0,
    ("eléctrico", "veneno"): 1.0,
    ("eléctrico", "tierra"): 0.0,
    ("eléctrico", "volador"): 2.0,
    ("eléctrico", "psíquico"): 1.0,
    ("eléctrico", "bicho"): 1.0,
    ("eléctrico", "roca"): 1.0,
    ("eléctrico", "dragón"): 0.5,
    ("eléctrico", "hielo"): 1.0,
    ("eléctrico", "eléctrico"): 0.5,
    
    #hielo
    ("hielo", "normal"): 1.0,
    ("hielo", "fuego"): 0.5,
    ("hielo", "agua"): 1.0,
    ("hielo", "planta"): 2.0,
    ("hielo", "fantasma"): 1.0,
    ("hielo", "lucha"): 1.0,
    ("hielo", "veneno"): 1.0,
    ("hielo", "tierra"): 2.0,
    ("hielo", "volador"): 2.0,
    ("hielo", "psíquico"): 1.0,
    ("hielo", "bicho"): 1.0,
    ("hielo", "roca"): 0.5,
    ("hielo", "dragón"): 2.0,
    ("hielo", "eléctrico"): 1.0,
    
    
    #dragón
    ("dragón", "normal"): 1.0,
    ("dragón", "fuego"): 1.0,
    ("dragón", "agua"): 1.0,
    ("dragón", "planta"): 1.0,
    ("dragón", "fantasma"): 1.0,
    ("dragón", "lucha"): 1.0,
    ("dragón", "veneno"): 1.0,
    ("dragón", "tierra"): 1.0,
    ("dragón", "volador"): 1.0,
    ("dragón", "psíquico"): 1.0,
    ("dragón", "bicho"): 1.0,
    ("dragón", "roca"): 1.0,
    ("dragón", "dragón"): 2.0,
    ("dragón", "hielo"): 0.5,
    ("dragón", "eléctrico"): 0.5,
    
    #fantasma
    ("fantasma", "normal"): 0.0,
    ("fantasma", "fuego"): 1.0,
    ("fantasma", "agua"): 1.0,
    ("fantasma", "planta"): 1.0,
    ("fantasma", "fantasma"): 2.0,
    ("fantasma", "lucha"): 1.0,
    ("fantasma", "veneno"): 1.0,
    ("fantasma", "tierra"): 1.0,
    ("fantasma", "volador"): 1.0,
    ("fantasma", "psíquico"): 1.0,
    ("fantasma", "bicho"): 1.0,
    ("fantasma", "roca"): 1.0,
    ("fantasma", "dragón"): 1.0,
    ("fantasma", "hielo"): 1.0,
    ("fantasma", "eléctrico"): 1.0,
    
    #lucha
    ("lucha", "normal"): 2.0,
    ("lucha", "fuego"): 1.0,
    ("lucha", "agua"): 1.0,
    ("lucha", "planta"): 1.0,
    ("lucha", "fantasma"): 0.5,
    ("lucha", "lucha"): 1.0,
    ("lucha", "veneno"): 0.5,
    ("lucha", "tierra"): 1.0,
    ("lucha", "volador"): 0.5,
    ("lucha", "psíquico"): 0.5,
    ("lucha", "bicho"): 0.5,
    ("lucha", "roca"): 2.0,
    ("lucha", "dragón"): 1.0,
    ("lucha", "hielo"): 2.0,
    ("lucha", "eléctrico"): 1.0,
    
    #veneno
    ("veneno", "normal"): 1.0,
    ("veneno", "fuego"): 1.0,
    ("veneno", "agua"): 1.0,
    ("veneno", "planta"): 2.0,
    ("veneno", "fantasma"): 1.0,
    ("veneno", "lucha"): 1.0,
    ("veneno", "veneno"): 0.5,
    ("veneno", "tierra"): 1.0,
    ("veneno", "volador"): 1.0,
    ("veneno", "psíquico"): 1.0,
    ("veneno", "bicho"): 2.0,
    ("veneno", "roca"): 1.0,
    ("veneno", "dragón"): 1.0,
    ("veneno", "hielo"): 1.0,
    ("veneno", "eléctrico"): 1.0,
    
    #tierra
    ("tierra", "normal"): 1.0,
    ("tierra", "fuego"): 2.0,
    ("tierra", "agua"): 1.0,
    ("tierra", "planta"): 0.5,
    ("tierra", "fantasma"): 1.0,
    ("tierra", "lucha"): 1.0,
    ("tierra", "veneno"): 2.0,
    ("tierra", "tierra"): 1.0,
    ("tierra", "volador"): 0.5,
    ("tierra", "psíquico"): 1.0,
    ("tierra", "bicho"): 1.0,
    ("tierra", "roca"): 2.0,
    ("tierra", "dragón"): 1.0,
    ("tierra", "hielo"): 1.0,
    ("tierra", "eléctrico"): 2.0,
    
    #volador
    ("volador", "normal"): 1.0,
    ("volador", "fuego"): 1.0,
    ("volador", "agua"): 1.0,
    ("volador", "planta"): 2.0,
    ("volador", "fantasma"): 1.0,
    ("volador", "lucha"): 2.0,
    ("volador", "veneno"): 1.0,
    ("volador", "tierra"): 1.0,
    ("volador", "volador"): 1.0,
    ("volador", "psíquico"): 1.0,
    ("volador", "bicho"): 2.0,
    ("volador", "roca"): 0.5,
    ("volador", "dragón"): 1.0,
    ("volador", "hielo"): 1.0,
    ("volador", "eléctrico"): 0.5,
    
    #bicho
    ("bicho", "normal"): 1.0,
    ("bicho", "fuego"): 0.5,
    ("bicho", "agua"): 1.0,
    ("bicho", "planta"): 2.0,
    ("bicho", "fantasma"): 1.0,
    ("bicho", "lucha"): 1.0,
    ("bicho", "veneno"): 0.5,
    ("bicho", "tierra"): 1.0,
    ("bicho", "volador"): 0.5,
    ("bicho", "psíquico"): 1.0,
    ("bicho", "bicho"): 1.0,
    ("bicho", "roca"): 0.5,
    ("bicho", "dragón"): 1.0,
    ("bicho", "hielo"): 1.0,
    ("bicho", "eléctrico"): 1.0,
    
    #roca
    ("roca", "normal"): 1.0,
    ("roca", "fuego"): 2.0,
    ("roca", "agua"): 1.0,
    ("roca", "planta"): 1.0,
    ("roca", "fantasma"): 1.0,
    ("roca", "lucha"): 0.5,
    ("roca", "veneno"): 1.0,
    ("roca", "tierra"): 1.0,
    ("roca", "volador"): 2.0,
    ("roca", "psíquico"): 1.0,
    ("roca", "bicho"): 2.0,
    ("roca", "roca"): 1.0,
    ("roca", "dragón"): 1.0,
    ("roca", "hielo"): 2.0,
    ("roca", "eléctrico"): 1.0,
    
    #psiquico
    ("psíquico", "normal"): 1.0,
    ("psíquico", "fuego"): 1.0,
    ("psíquico", "agua"): 1.0,
    ("psíquico", "planta"): 1.0,
    ("psíquico", "fantasma"): 1.0,
    ("psíquico", "lucha"): 2.0,
    ("psíquico", "veneno"): 1.0,
    ("psíquico", "tierra"): 1.0,
    ("psíquico", "volador"): 1.0,
    ("psíquico", "psíquico"): 1.0,
    ("psíquico", "bicho"): 1.0,
    ("psíquico", "roca"): 1.0,
    ("psíquico", "dragón"): 1.0,
    ("psíquico", "hielo"): 1.0,
    ("psíquico", "eléctrico"): 1.0
    }

# estructuras.py

class Ataque:
    """
    Representa un ataque con nombre, tipo y poder.
    """
    def __init__(self, nombre, tipo, poder):
        self.nombre = nombre
        self.tipo = tipo
        self.poder = poder

    def __str__(self):
        return f"{self.nombre} ({self.tipo}, Poder: {self.poder})"


class Pokemon:
    """
    Representa un Pokémon con nombre, tipo(s), etapa evolutiva, y ataques.
    """
    def __init__(self, nombre, tipos, ps, ataques=None):
        self.nombre = nombre
        self.tipos = tipos if isinstance(tipos, list) else [tipos]
        self.ps = ps  # ← ¡esta línea es clave!
        self.etapa = 1  # puedes mantenerlo fijo o usar otro parámetro si lo deseas
        self.ataques = ataques if ataques is not None else []

    def agregar_ataque(self, ataque):
        self.ataques.append(ataque)

    def esta_debilitado(self):
        return self.ps <= 0

    def __str__(self):
        tipos_str = "/".join(self.tipos)
        ataques_str = ", ".join(ataque.nombre for ataque in self.ataques)
        return f"{self.nombre} ({tipos_str}, {self.ps} PS) - Ataques: {ataques_str}"


class Entrenador:
    """
    Representa a un entrenador con un nombre y una lista de Pokémon.
    """
    def __init__(self, nombre, pokemones):
        self.nombre = nombre
        self.pokemones = pokemones
        self.indice_activo = 0  # Siempre inicia con el primer Pokémon

    def pokemon_activo(self):
        return self.pokemones[self.indice_activo]

    def tiene_pokemon_vivo(self):
        return any(p.ps > 0 for p in self.pokemones)

    def cambiar_pokemon(self):
        for i, p in enumerate(self.pokemones):
            if p.ps > 0:
                self.indice_activo = i
                return True
        return False  # Todos están debilitados
