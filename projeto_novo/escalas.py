NOTAS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
ESCALA = {'maior': [0, 2, 4, 5, 7, 9, 11]}


def escalas(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gerar uma escala a partir de uma tônica e uma tonalidade.

    Parameters:
        tonica: Nota que será a tônica da escala
        tonalidade: Tonalidade da escala

    Returns:
        Um dicionário com as notas da escala e graus
    
    Examples:    
        >>> escalas('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escalas('A', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    NOTAS_2 = [
        NOTAS[i % 12]
        for i in range(NOTAS.index(tonica), NOTAS.index(tonica) + 12)
    ]

    notas = [NOTAS_2[int] for int in ESCALA[tonalidade]]

    return {
        'notas': notas,
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
    ...
