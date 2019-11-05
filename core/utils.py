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
