ASCII_BRAILLE = {
    ' ': '⠀',
    '!': '⠮',
    '"': '⠐',
    '#': '⠼',
    '$': '⠫',
    '%': '⠩',
    '&': '⠯',
    "'": '⠄',
    '(': '⠷',
    ')': '⠾',
    '*': '⠡',
    '+': '⠬',
    ',': '⠠',
    '-': '⠤',
    '.': '⠨',
    '/': '⠌',
    ':': '⠱',
    ';': '⠰',
    '<': '⠣',
    '=': '⠿',
    '>': '⠜',
    '?': '⠹',
    '@': '⠈',

    '0': '⠴',
    '1': '⠂',
    '2': '⠆',
    '3': '⠒',
    '4': '⠲',
    '5': '⠢',
    '6': '⠖',
    '7': '⠶',
    '8': '⠦',
    '9': '⠔',

    'a': '⠁',
    'b': '⠃',
    'c': '⠉',
    'd': '⠙',
    'e': '⠑',
    'f': '⠋',
    'g': '⠛',
    'h': '⠓',
    'i': '⠊',
    'j': '⠚',
    'k': '⠅',
    'l': '⠇',
    'm': '⠍',
    'n': '⠝',
    'o': '⠕',
    'p': '⠏',
    'q': '⠟',
    'r': '⠗',
    's': '⠎',
    't': '⠞',
    'u': '⠥',
    'v': '⠧',
    'w': '⠺',
    'x': '⠭',
    'y': '⠽',
    'z': '⠵',

    'ç': '⠉',
    'á': '⠷',
    'é': '⠮',
    'í': '⠌',
    'ó': '⠬',
    'ú': '⠜',
    'â': '⠆',
    'ê': '⠖',
    'î': '⠦',
    'ô': '⠔',
    'û': '⠣',
    'ã': '⠯',
    'õ': '⠹',
    'à': '⠸',
    'è': '⠌',
    'ì': '⠜',
    'ò': '⠰',
    'ù': '⠔',
    '[': '⠪',
    '\\': '⠳',
    ']': '⠻',
    '^': '⠘',
    '_': '⠸',
}


def text_to_braille(text):
    """
    Converte texto em ASCII para braile utilizando o dicionário de mapeamento

    :param text: Texto a ser convertido
    :return: Texto em braille
    """

    final_string = ''
    for char in text.lower():
        final_string += ASCII_BRAILLE.get(char, '')  # Usa um valor padrão vazio se o caractere não for encontrado
    return final_string
