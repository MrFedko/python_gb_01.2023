def num_of_words(text: str):
    result = sorted(text.split())
    [print(f"{i} {word:>{len(max(result, key=len))}}") for i, word in enumerate(result, 1)]
