# 1.3 - Modifique o teste negativo para que leia valores de uma lista

import pytest

from calculo_racao_p_m_g import cao_p, cao_m

# Tupla para calculadora Pet racao diaria
lista_peso_pet_peso_racao_cao_p = [
    (13, 10, 130),
    (10, 10, 100),
    (9, 10, 90),
    (0, 10, 0),
    (16, 10, 160),
    (.6, 10, 6)
]

lista_peso_pet_peso_racao_cao_m = [
    (16, 20, 320),
    (17, 20, 340),
    (20, 20, 400),
    (9, 20, 180),
    (0, 20, 0),
    (27, 20, 540)
]


@pytest.mark.parametrize('peso_pet, peso_racao, resultado_esperado', lista_peso_pet_peso_racao_cao_p)

# Pet de pequeno porte de 1 a 15 kilos
def test_cao_pequeno(peso_pet, peso_racao, resultado_esperado):
    # 1 - Configura
    # n1 peso do pet
    # n2 gramas de ração
    # n1 = peso_pet
    # n2 = peso_racao
    # resultado = n1*n2
    # 2 - Executa
    result_obitido = cao_p(peso_pet, peso_racao)
    # 3 - Valida
    assert resultado_esperado == result_obitido



@pytest.mark.parametrize('peso_pet_m, peso_racao_m, resultado_esperado_m', lista_peso_pet_peso_racao_cao_m)
# Pet de médio porte de # 20g para M 15 a 25
def test_cao_medio(peso_pet_m, peso_racao_m, resultado_esperado_m):
    # 1 - Configura
    # n1 peso do pet
    # n2 gramas de ração
    # n1 = peso_pet
    # n2 = peso_racao
    # resultado = n1*n2
    # 2 - Executa
    result_obitido = cao_m(peso_pet_m, peso_racao_m)
    # 3 - Valida
    assert resultado_esperado_m == result_obitido





