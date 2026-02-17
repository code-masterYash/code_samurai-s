def convert_seconds(total_seconds: int) -> str:
    total_seconds = int(total_seconds)
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes}m {seconds}s"


if __name__ == "__main__":
    time_input = int(input("Enter total seconds: "))
    result = convert_seconds(time_input)
    print("Converted time:", result)
