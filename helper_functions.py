import numpy as np


def convert_english_text(input_text) -> tuple[np.ndarray, str, str]:
    latin_letters = ['F', 'U', 'TH', 'O', 'R', 'C', 'G', 'W', 'H', 'N', 'I', 'J', 'EO', 'P', 'X', 'S', 'T', 'B', 'E',
                     'M', 'L', 'ING', 'OE', 'D', 'A', 'AE', 'Y', 'IA', 'EA']
    runes = ['ᚠ', 'ᚢ', 'ᚦ', 'ᚩ', 'ᚱ', 'ᚳ', 'ᚷ', 'ᚹ', 'ᚻ', 'ᚾ', 'ᛁ', 'ᛄ', 'ᛇ', 'ᛈ', 'ᛉ', 'ᛋ', 'ᛏ', 'ᛒ', 'ᛖ', 'ᛗ', 'ᛚ',
             'ᛝ', 'ᛟ', 'ᛞ', 'ᚪ', 'ᚫ', 'ᚣ', 'ᛡ', 'ᛠ']

    e2p = {}
    for i in range(0, 29):
        e2p[latin_letters[i]] = i
    e2p["IO"] = e2p["IA"]
    e2p["K"] = e2p["C"]
    e2p["NG"] = e2p["ING"]
    e2p["Z"] = e2p["S"]
    e2p["Q"] = e2p["C"]
    e2p["V"] = e2p["U"]

    input_text = input_text.upper().replace("QU", "KW")
    input_text = input_text.replace("Q", "K")

    text_as_index = []
    text_as_gematria = ''
    text_as_runes = ''

    skip = 0

    for index, value in enumerate(input_text):
        if skip:
            skip -= 1
            continue

        if value == ' ':
            text_as_gematria += value
            text_as_runes += value
            continue

        elif (index < len(input_text) - 3) and (input_text[index:index + 3] in e2p):
            result = input_text[index:index + 3]
            skip = 2

        elif (index < len(input_text) - 2) and (input_text[index:index + 2] in e2p):
            result = input_text[index:index + 2]
            skip = 1

        else:
            result = input_text[index]

        text_as_index.append(e2p[result])
        text_as_gematria += latin_letters[e2p[result]]
        text_as_runes += runes[e2p[result]]

    return np.asarray(text_as_index), text_as_gematria, text_as_runes


def gp_values(input_array: np.ndarray) -> np.ndarray:
    gp = np.array(
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
         109])
    return gp[input_array]


def gp_sum(input_str: str) -> int:
    text_as_indices, _, _ = convert_english_text(input_str, )
    gp = gp_values(text_as_indices)
    return sum(gp)
