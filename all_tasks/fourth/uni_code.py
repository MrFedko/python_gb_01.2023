def uni_code(text: str) -> list[int]:
    return sorted([ord(i) for i in set(text)], reverse=True)
