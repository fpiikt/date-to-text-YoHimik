from .consts import NUMBERS, THOUSANDS
from .getUnitsForNumber import *


def get_thousands(number):
    thousands = number // 1000
    if thousands == 0:
        return None
    else:
        num_word = NUMBERS[thousands]
        first_word = num_word['fem'] if isinstance(num_word, dict) else num_word
        second_word = get_units_for_number(thousands, THOUSANDS)
        return f'{first_word} {second_word}'
