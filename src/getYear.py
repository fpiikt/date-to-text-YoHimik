from .consts import YEAR_PREFIXES, TEN_ROUNDS, TENTH, YEAR_ENDS
from .getThousands import get_thousands
from .getUnits import get_hundreds, get_tens


def get_year(number):
    year_words = []

    if number % 1000 == 0 and number // 1000 is not 0:
        thousands = number // 1000
        return f'{YEAR_PREFIXES[thousands]}тысячного'
    else:
        year_words.insert(0, get_thousands(number))

    if number % 100 == 0 and number // 100 is not 0:
        hundreds = number // 100
        if hundreds >= 10:
            hundreds = hundreds % 10
        return f'{YEAR_PREFIXES[hundreds]}сотого' if year_words[
                                                         0] is None else f'{year_words[0]} {YEAR_PREFIXES[hundreds]}сотого'
    else:
        year_words.insert(1, get_hundreds(number))
    if number % 10 == 0 and number // 10 is not 0:
        decades = (number // 10) % 10
        year_words.insert(2, TEN_ROUNDS[decades])
        return ' '.join([x for x in year_words if x is not None])
    elif 10 < (number % 100) < 20:  # teens
        year_words.insert(2, f'{TENTH[number % 100][:-1]}ого')
        return ' '.join([x for x in year_words if x is not None])
    else:
        year_words.insert(2, get_tens(number))
    year = number % 10
    year_words.insert(3, YEAR_ENDS[year])
    return ' '.join([x for x in year_words if x is not None])
