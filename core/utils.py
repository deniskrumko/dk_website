from datetime import datetime

MONTH_LIST = [
    'Январь',
    'Февраль',
    'Март',
    'Апрель',
    'Май',
    'Июнь',
    'Июль',
    'Август',
    'Сентябрь',
    'Октябрь',
    'Ноябрь',
    'Декабрь',
]

WEEKDAY_LIST = [
    'Понедельник',
    'Вторник',
    'Среда',
    'Четверг',
    'Пятница',
    'Суббота',
    'Воскресенье',
]


def time_str_to_int(value: str) -> int:
    """Convert time as string to integer (seconds)."""
    minutes, seconds = value.split(':')
    return int(minutes) * 60 + int(seconds)


def time_int_to_str(value: int) -> str:
    """Convert integer (seconds) to time as string."""
    if not value:
        return '00:00'

    minutes = str(value // 60).zfill(2)
    seconds = str(value % 60).zfill(2)

    return f'{minutes}:{seconds}'


def ru_date_format(date, format_str) -> str:
    """Format date with russian tags.

    Available tags:
        %RSM - russian short month
        %RFM - russian full month
        %RXM - russian full month (with correct ending)
        %RWD - russian weekday
    """
    if '%RSM' in format_str:
        short_name = MONTH_LIST[date.month - 1][:3].lower()
        format_str = format_str.replace('%RSM', short_name)

    if '%RFM' in format_str:
        full_name = MONTH_LIST[date.month - 1]
        format_str = format_str.replace('%RFM', full_name)

    if '%RXM' in format_str:
        full_name = MONTH_LIST[date.month - 1]
        if full_name[-1] in ('ь', 'й'):
            full_name = full_name[:-1] + 'я'
        else:
            full_name += 'а'

        format_str = format_str.replace('%RXM', full_name)

    if '%RWD' in format_str:
        weekday = WEEKDAY_LIST[date.weekday()]
        format_str = format_str.replace('%RWD', weekday)

    return datetime.strftime(date, format_str)
