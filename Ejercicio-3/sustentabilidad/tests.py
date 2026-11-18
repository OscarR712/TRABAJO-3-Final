
import unittest

from .funcs import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_nominal_por_defecto(self):
        resultado = calcular_emisiones_carbono(100.0)
        self.assertAlmostEqual(resultado, 40.0)

    def test_calculo_con_factor_personalizado(self):
        resultado = calcular_emisiones_carbono(
            200.0,
            factor_emision=0.5
        )
        self.assertAlmostEqual(resultado, 100.0)

    def test_consumo_cero(self):
        resultado = calcular_emisiones_carbono(0.0)
        self.assertEqual(resultado, 0.0)

    def test_consumo_negativo_eleva_excepcion(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50.0)
