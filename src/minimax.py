# minimax.py

from estructuras import Pokemon, Ataque
from combate import calcular_danio
import copy

MAX_PROFUNDIDAD = 2  # Puedes ajustar esta profundidad

class EstadoCombate:
    """
    Representa un estado del combate con copias independientes de los Pokémon.
    """
    def __init__(self, pokemon_ia: Pokemon, pokemon_jugador: Pokemon):
        self.pokemon_ia = copy.deepcopy(pokemon_ia)
        self.pokemon_jugador = copy.deepcopy(pokemon_jugador)

    def esta_terminado(self):
        return self.pokemon_ia.ps <= 0 or self.pokemon_jugador.ps <= 0


def evaluar_estado(estado: EstadoCombate) -> int:
    """
    Evalúa un estado del combate desde la perspectiva de la IA.
    """
    if estado.pokemon_ia.ps <= 0:
        return -1000  # Derrota
    if estado.pokemon_jugador.ps <= 0:
        return 1000   # Victoria

    # Heurística simple: diferencia de PS
    return estado.pokemon_ia.ps - estado.pokemon_jugador.ps


def simular_ataque(estado: EstadoCombate, es_ia: bool, ataque: Ataque) -> EstadoCombate:
    """
    Simula el resultado de un ataque y devuelve un nuevo estado del combate.
    """
    nuevo_estado = EstadoCombate(estado.pokemon_ia, estado.pokemon_jugador)
    atacante = nuevo_estado.pokemon_ia if es_ia else nuevo_estado.pokemon_jugador
    defensor = nuevo_estado.pokemon_jugador if es_ia else nuevo_estado.pokemon_ia

    danio = calcular_danio(atacante, ataque, defensor)
    defensor.ps -= danio
    if defensor.ps < 0:
        defensor.ps = 0

    return nuevo_estado


def minimax(estado: EstadoCombate, profundidad: int, maximizando: bool, alpha: float, beta: float):
    """
    Algoritmo minimax con poda alfa-beta.
    """
    if profundidad == 0 or estado.esta_terminado():
        return evaluar_estado(estado), None

    if maximizando:
        max_eval = float('-inf')
        mejor_ataque = None
        for ataque in estado.pokemon_ia.ataques:
            nuevo_estado = simular_ataque(estado, True, ataque)
            eval, _ = minimax(nuevo_estado, profundidad - 1, False, alpha, beta)
            if eval > max_eval:
                max_eval = eval
                mejor_ataque = ataque
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, mejor_ataque
    else:
        min_eval = float('inf')
        peor_ataque = None
        for ataque in estado.pokemon_jugador.ataques:
            nuevo_estado = simular_ataque(estado, False, ataque)
            eval, _ = minimax(nuevo_estado, profundidad - 1, True, alpha, beta)
            if eval < min_eval:
                min_eval = eval
                peor_ataque = ataque
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, peor_ataque


def elegir_mejor_ataque(pokemon_ia: Pokemon, pokemon_jugador: Pokemon) -> Ataque:
    """
    Función principal para que la IA elija su mejor movimiento.
    """
    estado_inicial = EstadoCombate(pokemon_ia, pokemon_jugador)
    _, mejor_ataque = minimax(estado_inicial, MAX_PROFUNDIDAD, True, float('-inf'), float('inf'))
    return mejor_ataque
