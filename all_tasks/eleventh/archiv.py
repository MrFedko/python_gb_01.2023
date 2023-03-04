class Archive:
    """При первом запуске создает экземпляр класса, при повторном - добавляет в архив прежние данные."""
    instance = None
    counts = []
    texts = []

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        else:
            cls.instance.counts.append(cls.instance.count)
            cls.instance.texts.append(cls.instance.text)
        return cls.instance

    def __init__(self, count, text):
        self.count = count
        self.text = text

    def __str__(self):
        c = self.instance.counts if self.instance.counts else "Empty"
        t = self.instance.texts if self.instance.texts else "Empty"
        return f"Value: {self.instance.count}, text: {self.instance.text} " \
    f"value archive: {c}, text archive: {t}"

    def __repr__(self):
        return f"Archive({self.instance.count}, '{self.instance.text}')"


if __name__ == '__main__':
    d1 = Archive(1, 'a')
    print(d1.text, d1.texts)
    print(f'{d1}')
    print(f'{d1 =}')
    d2 = Archive(2, "b")
    print(d2.text, d2.texts)
    print(f'{d2}')
    print(f'{d2 =}')

