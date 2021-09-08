import time


def get_human_timestamp(timestamp: float) -> str:
    delta = int(time.time() - timestamp)
    plural = "s" if 1 < delta < 60 or delta > 60 else ""
    time_name = "second" if 0 <= delta < 60 else "minute"
    if delta >= 60:
        delta //= 60
    return f"{delta} {time_name}{plural} ago"