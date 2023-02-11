# 1.2 - Crie pelo menos um teste positivo e outro negativo para essa
# 1.3 - Modifique o teste negativo para que leia valores de uma lista
# 1.4 - Modifique o teste positivo para que leia um arquivo CSV

from calculo_racao_p_m_g import cao_p, cao_m, cao_g, cao_gg

class TesteCalculador:
    # Pet de pequeno porte de 1 a 15 kilos
    def test_cao_pequeno_positivo(self):
        # 1 - Configura
        # n1 peso do pet
        # n2 gramas de ração
        n1 = 14
        n2 = 10
        resultado = n1*n2
        # 2 - Executa
        result_obitido = cao_p(n1, n2)
        # 3 - Valida
        assert resultado == result_obitido


    def test_cao_pequeno_negativo_peso_zero(self):
        # 1 - Configura
        # n1 peso do pet
        # n2 gramas de ração
        n1 = 0
        n2 = 10
        resultado = n1*n2
        # 2 - Executa
        result_obitido = cao_p(n1, n2)
        # 3 - Valida
        assert resultado == result_obitido

    def test_cao_pequeno_negativo_peso_fora_do_porte_a_menos(self):
        # 1 - Configura
        # n1 peso do pet
        # n2 gramas de ração
        n1 = .5
        n2 = 10
        resultado = n1*n2
        # 2 - Executa
        result_obitido = cao_p(n1, n2)
        # 3 - Valida
        assert resultado == result_obitido

    def test_cao_pequeno_negativo_peso_fora_do_porte_a_mais(self):
        # 1 - Configura
        # n1 peso do pet
        # n2 gramas de ração
        n1 = 16
        n2 = 10
        resultado = n1*n2
        # 2 - Executa
        result_obitido = cao_p(n1, n2)
        # 3 - Valida
        assert resultado == result_obitido

    # Pet de médio porte de 15 a 25 kilos
    def test_cao_medio_positivo(self):
        # 1 - Configura
        # n1 peso do pet
        # n2 gramas de ração
        n1 = 17
        n2 = 20
        resultado = n1*n2
        # 2 - Executa
        result_obitido = cao_m(n1, n2)
        # 3 - Valida
        assert resultado == result_obitido


    def test_cao_medio_negativo_peso_zero(self):
        # 1 - Configura
        # n1 peso do pet
        # n2 gramas de ração
        n1 = 0
        n2 = 20
        resultado = n1*n2
        # 2 - Executa
        result_obitido = cao_m(n1, n2)
        # 3 - Valida
        assert resultado == result_obitido

    def test_cao_medio_negativo_peso_fora_do_porte_a_menos(self):
        # 1 - Configura
        # n1 peso do pet
        # n2 gramas de ração
        n1 = 14
        n2 = 20
        resultado = n1*n2
        # 2 - Executa
        result_obitido = cao_m(n1, n2)
        # 3 - Valida
        assert resultado == result_obitido

    def test_cao_medio_negativo_peso_fora_do_porte_a_mais(self):
        # 1 - Configura
        # n1 peso do pet
        # n2 gramas de ração
        n1 = 26
        n2 = 20
        resultado = n1*n2
        # 2 - Executa
        result_obitido = cao_m(n1, n2)
        # 3 - Valida
        assert resultado == result_obitido

    # Pet de grande porte 25 a 45 kilos
    def test_cao_grande_positivo(self):
        # 1 - Configura
        # n1 peso do pet
        # n2 gramas de ração
        n1 = 30
        n2 = 30
        resultado = n1*n2
        # 2 - Executa
        result_obitido = cao_g(n1, n2)
        # 3 - Valida
        assert resultado == result_obitido


    def test_cao_grande_negativo_peso_zero(self):
        # 1 - Configura
        # n1 peso do pet
        # n2 gramas de ração
        n1 = 0
        n2 = 30
        resultado = n1*n2
        # 2 - Executa
        result_obitido = cao_g(n1, n2)
        # 3 - Valida
        assert resultado == result_obitido

    def test_cao_grande_negativo_peso_fora_do_portefora_do_porte_a_menos(self):
        # 1 - Configura
        # n1 peso do pet
        # n2 gramas de ração
        n1 = 22
        n2 = 30
        resultado = n1*n2
        # 2 - Executa
        result_obitido = cao_g(n1, n2)
        # 3 - Valida
        assert resultado == result_obitido

    def test_cao_grande_negativo_peso_fora_do_portefora_do_porte_a_mais(self):
        # 1 - Configura
        # n1 peso do pet
        # n2 gramas de ração
        n1 = 46
        n2 = 30
        resultado = n1*n2
        # 2 - Executa
        result_obitido = cao_g(n1, n2)
        # 3 - Valida
        assert resultado == result_obitido

    # Pet de gigante porte 45 a 90 kilos
    def test_cao_gigante_positivo(self):
        # 1 - Configura
        # n1 peso do pet
        # n2 gramas de ração
        n1 = 50
        n2 = 45
        resultado = n1*n2
        # 2 - Executa
        result_obitido = cao_gg(n1, n2)
        # 3 - Valida
        assert resultado == result_obitido


    def test_cao_gigante_negativo_peso_zero(self):
        # 1 - Configura
        # n1 peso do pet
        # n2 gramas de ração
        n1 = 0
        n2 = 45
        resultado = n1*n2
        # 2 - Executa
        result_obitido = cao_gg(n1, n2)
        # 3 - Valida
        assert resultado == result_obitido

    def test_cao_gigante_negativo_peso_fora_do_porte_a_menos(self):
        # 1 - Configura
        # n1 peso do pet
        # n2 gramas de ração
        n1 = 30
        n2 = 45
        resultado = n1*n2
        # 2 - Executa
        result_obitido = cao_gg(n1, n2)
        # 3 - Valida
        assert resultado == result_obitido

    def test_cao_gigante_negativo_peso_fora_do_porte_a_mais(self):
        # 1 - Configura
        # n1 peso do pet
        # n2 gramas de ração
        n1 = 100
        n2 = 45
        resultado = n1*n2
        # 2 - Executa
        result_obitido = cao_gg(n1, n2)
        # 3 - Valida
        assert resultado == result_obitido


