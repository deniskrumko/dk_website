def time_str_to_int(value: str) -> int:
    minutes, seconds = value.split(':')
    return int(minutes) * 60 + int(seconds)


def time_int_to_str(value: int) -> str:
    if not value:
        return '00:00'

    minutes = str(value // 60).zfill(2)
    seconds = str(value % 60).zfill(2)

    return f'{minutes}:{seconds}'
