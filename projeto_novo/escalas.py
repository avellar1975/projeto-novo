NOTAS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
INTERVALOS = [0, 2, 4, 5, 7, 9, 11]


def escalas(tonica, tonalidade):
    """
    >>> escalas('C', 'maior')
    {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    >>> escalas('A', 'maior')
    {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    notas = []
    NOTAS_2 = [
        NOTAS[i % 12]
        for i in range(NOTAS.index(tonica), NOTAS.index(tonica) + 12)
    ]

    for int in INTERVALOS:
        notas.append(NOTAS_2[int])
    return {
        'notas': notas,
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
    ...
