NOTAS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
ESCALA = {'maior': [0, 2, 4, 5, 7, 9, 11]}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gerar uma escala a partir de uma tônica e uma tonalidade.

    Parameters:
        tonica: Nota que será a tônica da escala
        tonalidade: Tonalidade da escala

    Returns:
        Um dicionário com as notas da escala e graus

    Raises:
        ValueError: Caso a tônica não seja uma nota válida.
        KeyError: Caso a escala não exista ou não tenha sido implementada.

    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('a', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.upper()
    try:
        NOTAS_2 = [
            NOTAS[i % 12]
            for i in range(NOTAS.index(tonica), NOTAS.index(tonica) + 12)
        ]
        notas = [NOTAS_2[int] for int in ESCALA[tonalidade]]
    except ValueError:
        raise ValueError(f'Essa nota não existe, tente uma dessas {NOTAS}')
    except KeyError:
        raise KeyError(
            'Essa escala não existe ou não foi implementada.'
            f'Tente uma dessas {list(ESCALA.keys())}'
        )
    return {
        'notas': notas,
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
    ...
