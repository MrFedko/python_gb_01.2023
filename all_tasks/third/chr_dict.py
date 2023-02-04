def chr_dict(text: str) -> dict[str:int]:
    return {char: text.count(char) for char in text}

