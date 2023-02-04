import re


def reformat(text: str) -> (int, float, str):
    if text.isdigit() and int(text) >= 0:
        return int(text)
    elif re.match(r'^-?\d+(?:\.\d+)$', text):
        return float(text)
    else:
        return text.lower()
