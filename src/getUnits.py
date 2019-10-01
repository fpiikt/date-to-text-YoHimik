from .consts import DAYS, MONTHS, HUNDREDS, TENS


def get_hundreds(number):
    hundreds = number // 100 % 10
    if hundreds == 0:
        return None
    return HUNDREDS[hundreds]


def get_tens(number):
    tens = number // 10 % 10
    return None if tens == 0 else TENS[tens]


def get_day(number):
    return DAYS[number]


def get_month(number):
    return MONTHS[number]
