"""
  Автор: Федюкович Семён, группа №P3255

"""

from src.getUnitsForNumber import *
from src.consts import *
from src.getUnits import *
from src.getYear import *
from src.getTimeNumber import *


def convert(date_string: str) -> str:
    """

    :type date_string: str: Datetime in format DD.MM.YYYY hh:mm:ss
    """
    day_time = date_string.split(' ')
    if len(day_time) != 2:
        return None
    [date, time] = day_time

    day_months_year = [int(x) for x in date.split('.')]
    if len(day_months_year) != 3:
        return None
    [day, month, year] = day_months_year

    hours_minutes_seconds = [int(x) for x in time.split(':')]
    if len(hours_minutes_seconds) != 3:
        return None
    [hours, minutes, seconds] = hours_minutes_seconds

    if day < 0 or day > 31:
        return None
    if month < 0 or month > 12:
        return None
    if year < 0 or year > 9999:
        return None
    if hours < 0 or hours > 24:
        return None
    if minutes < 0 or minutes > 60:
        return None
    if seconds < 0 or seconds > 60:
        return None

    hours_units = get_units_for_number(hours, HOURS)
    minutes_units = get_units_for_number(minutes, MINUTES)
    seconds_units = get_units_for_number(seconds, SECONDS)
    day_word = DAYS[day]
    month_word = MONTHS[month]
    year_word = get_year(year)
    hours_word = get_time_number(hours, 'mus')
    minutes_word = get_time_number(minutes, 'fem')
    seconds_word = get_time_number(seconds, 'fem')
    return f'{day_word} {month_word} {year_word} года {hours_word} {hours_units} {minutes_word} {minutes_units} {seconds_word} {seconds_units}'
