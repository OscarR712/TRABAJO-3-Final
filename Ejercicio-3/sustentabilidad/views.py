
from django.shortcuts import render

from .funcs import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):

    registros_industriales = [
        {
            "planta": "Planta Las Heras",
            "consumo_kwh": 3400.0
        },
        {
            "planta": "Planta Godoy Cruz",
            "consumo_kwh": 1850.0
        },
        {
            "planta": "Planta Luján",
            "consumo_kwh": 4100.0
        }
    ]

    metricas = obtener_metricas_consumo(registros_industriales)

    contexto = {
        "titulo": "Panel de Sustentabilidad Industrial",
        "emisiones_totales": metricas["total_emisiones"],
        "planta_critica": metricas["planta_mayor_consumo"],
        "max_consumo_kwh": metricas["max_consumo_kwh"],
        "registros": registros_industriales
    }

    return render(
        request,
        "sustentabilidad/panel.html",
        contexto
    )
