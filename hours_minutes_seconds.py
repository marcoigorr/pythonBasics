def get_hours_minutes_seconds(_seconds) -> str:
    # Vars
    hours = 0
    minutes = 0
    seconds = _seconds
    time = ''

    # Operations
    if _seconds == 0:
        return f'{_seconds}s are 0s'

    minutes = seconds // 60
    seconds %= 60

    if minutes >= 60:
        hours = minutes // 60
        minutes = minutes % 60

    # String formatting
    if hours > 0:
        time += f'{hours}h '
    if minutes > 0:
        time += f'{minutes}m '
    if seconds > 0:
        time += f'{seconds}s '

    return f'{_seconds}s are {time}'
