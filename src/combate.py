
from estructuras import Pokemon, Ataque, efectividad

def calcular_efectividad(tipo_ataque: str, tipo_objetivo: str) -> float:
    return efectividad.get((tipo_ataque, tipo_objetivo), 1.0)

def calcular_danio(atacante: Pokemon, ataque: Ataque, defensor: Pokemon) -> int:
    efectividad = calcular_efectividad(ataque.tipo, defensor.tipo)
    danio_base = ataque.poder
    danio_total = int(danio_base * efectividad)
    
    print(f"{atacante.nombre} usa {ataque.nombre} ({ataque.tipo})")
    print(f"Efectividad: {efectividad}x")
    print(f"Daño infligido: {danio_total} PS\n")
    
    return danio_total

def aplicar_danio(defensor: Pokemon, danio: int):
    defensor.ps -= danio
    if defensor.ps < 0:
        defensor.ps = 0

def turno(atacante: Pokemon, defensor: Pokemon, ataque: Ataque):
    danio = calcular_danio(atacante, ataque, defensor)
    aplicar_danio(defensor, danio)
    if defensor.esta_debilitado():
        print(f"{defensor.nombre} ha sido debilitado.")
    else:
        print(f"{defensor.nombre} tiene {defensor.ps} PS restantes.\n")
