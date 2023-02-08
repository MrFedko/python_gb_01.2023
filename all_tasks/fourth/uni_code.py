def uni_code(text: str) -> list[int]:
    return sorted(set([ord(i) for i in text]), reverse=True)
