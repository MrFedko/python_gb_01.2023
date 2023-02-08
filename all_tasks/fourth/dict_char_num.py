def dict_char_num(text: str) -> dict[str:int]:
    minimum, maximum = sorted([int(i) for i in text.split()])
    return {chr(i): i for i in range(minimum, maximum + 1)}
