from estructuras import Pokemon, Ataque, efectividad

def calcular_efectividad(tipo_ataque: str, tipo_objetivo: str) -> float:
    return efectividad.get((tipo_ataque.lower(), tipo_objetivo.lower()), 1.0)

def calcular_danio(atacante: Pokemon, ataque: Ataque, defensor: Pokemon) -> int:
    # Calcular efectividad total considerando todos los tipos del defensor
    efectividad_total = 1.0
    for tipo_def in defensor.tipos:
        efectividad_total *= calcular_efectividad(ataque.tipo, tipo_def)

    danio_base = ataque.poder
    danio_total = int(danio_base * efectividad_total)
    
    print(f"{atacante.nombre} usa {ataque.nombre} ({ataque.tipo})")
    print(f"Efectividad total: {efectividad_total:.2f}x")
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
