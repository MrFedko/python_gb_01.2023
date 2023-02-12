def dict_with_int(text: str) -> dict[int:int]:
    first, second, third, *another = (int(i) for i in text.split("/"))
    return {second: first, third: tuple(another)}
