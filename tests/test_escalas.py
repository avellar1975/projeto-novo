"""
AAA - 3A - A3

Arange - Act - Assets!
Arrumar - Agir - Garantir!
"""
from pytest import mark, raises

from projeto_novo.escalas import ESCALA, NOTAS, escala


def test_escala_deve_funcionar_com_notas_minusculas():
    # Arrumar
    tonica = 'c'
    tonalidade = 'maior'

    # Ação
    result = escala(tonica, tonalidade)

    # Assert
    assert result


def test_deve_retornar_um_erro_que_a_nota_nao_existe():
    tonalidade = 'maior'
    tonica = 'x'
    mensagem_de_erro = f'Essa nota não existe, tente uma dessas {NOTAS}'

    with raises(ValueError) as error:
        escala(tonica, tonalidade)
    assert error.value.args[0] == mensagem_de_erro


def test_deve_retornar_um_erro_que_a_escala_nao_existe():
    tonica = 'c'
    tonalidade = 'tonalidade'

    mensagem_de_erro = (
        'Essa escala não existe ou não foi implementada.'
        f'Tente uma dessas {list(ESCALA.keys())}'
    )

    with raises(KeyError) as error:
        escala(tonica, tonalidade)
    assert error.value.args[0] == mensagem_de_erro


@mark.parametrize(
    'tonica, esperado',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
    ],
)
def test_deve_retornar_as_notas_corretas(tonica, esperado):
    resultado = escala(tonica, 'maior')
    assert resultado['notas'] == esperado


def test_deve_retornar_os_sete_graus():
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    resultado = escala('c', 'maior')
    resultado['graus'] == esperado
