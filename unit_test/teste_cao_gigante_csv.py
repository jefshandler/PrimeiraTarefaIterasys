# 1.4 - Modifique o teste positivo para que leia um arquivo CSV

import pytest
import csv
from calculo_racao_p_m_g import cao_gg

def read_csv_file(arquivo_csv):
    dados_cvs = []
    try:
        with open(arquivo_csv, newline='') as massa:
            campos = csv.reader(massa, delimiter=',')
            next(campos)
            for linha in campos:
                dados_cvs.append(linha)
            return dados_cvs
    except FileNotFoundError:
        print(f'Arquivo de massa de dados não encontrado para o teste: {arquivo_csv}')
    except Exception as fail:
        print(f'Falha catastrofica: {fail}')


@pytest.mark.parametrize('peso_pet_gg, peso_racao_gg, resultado_esperado_gg', read_csv_file(r'..\vendors\csv\massa_pet_gigante.csv'))
def test_cao_medio(peso_pet_gg, peso_racao_gg, resultado_esperado_gg):
    # 1 - Configura
    # n1 peso do pet
    # n2 gramas de ração
    # n1 = peso_pet
    # n2 = peso_racao
    # resultado = n1*n2
    # 2 - Executa
    result_obitido = cao_gg(int(peso_pet_gg), int(peso_racao_gg))
    # 3 - Valida
    assert int(resultado_esperado_gg) == int(result_obitido)



