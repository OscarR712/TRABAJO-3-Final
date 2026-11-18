
def calcular_emisiones_carbono(consumo_kwh: float, factor_emision: float = 0.4) -> float:
    if consumo_kwh < 0:
        raise ValueError("El consumo en kWh no puede ser un valor negativo.")

    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros: list) -> dict:
    total_emisiones_global = 0.0
    mayor_consumo = None
    planta_mayor = None

    for reg in registros:
        planta = reg.get("planta")
        consumo = reg.get("consumo_kwh", 0.0)

        emisiones = calcular_emisiones_carbono(consumo)
        total_emisiones_global += emisiones

        if mayor_consumo is None or consumo > mayor_consumo:
            mayor_consumo = consumo
            planta_mayor = planta

    return {
        "total_emisiones": total_emisiones_global,
        "planta_mayor_consumo": planta_mayor,
        "max_consumo_kwh": mayor_consumo if mayor_consumo is not None else 0
    }
