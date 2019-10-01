def get_units_for_number(number, words):
    if 10 <= number <= 20:
        return words['plural']
    remainder = number % 10
    if remainder == 1:
        return words['singular']
    if 2 <= remainder <= 4:
        return words['plural_alt']
    return words['plural']
