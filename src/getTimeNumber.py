from .consts import TENS, TENTH, NUMBERS


def get_time_number(number, gender):
    time_words = []
    if number == 0:
        return 'ноль'
    elif number < 10:
        time_words.insert(0, 'ноль')
        last_digit = number
    elif number % 10 == 0:
        return TENS[number // 10]
    elif 10 < number < 20:
        return TENTH[number]
    else:
        tens = number // 10
        time_words.insert(0, TENS[tens])
        last_digit = number % 10
    num_word = NUMBERS[last_digit]
    word = num_word[gender] if isinstance(num_word, dict) else num_word
    time_words.insert(1, word)
    return ' '.join(time_words)
