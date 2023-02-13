__all__ = ['next_variants', 'get_play']
all_variants = {}


def next_variants(question=None, answers=None) -> dict[str:str]:
    if question is not None:
        all_variants[question] = answers
    return all_variants


def get_play(varias: dict) -> None:
    [one_hundred_for_one(i, j) for i, j in varias.items()]


def one_hundred_for_one(question: str, answers: list[str], count=3) -> int:
    other_count = 0
    while other_count < count:
        print(question)
        from_user = input("Ваш вариант: ")
        other_count += 1
        if from_user.capitalize() in answers:
            return other_count
    return 0


if __name__ == '__main__':
    text = "Как зовут преподавателя?"
    variants = ["Михаил", "Алексей", "Анна", "C3po"]
    next_variants(text, variants)
    text = "Когда начнется курс Java?"
    variants = ["Июнь", "Июль", "Никогда"]
    next_variants(text, variants)
    get_play(next_variants())
