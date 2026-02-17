def convert_seconds(total_seconds: int) -> str:
    total_seconds = int(total_seconds)
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes}m {seconds}s"


