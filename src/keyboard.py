from src.item import Item


class Mixin_language:

    def __init__(self):
        self._language = None

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"


class Keyboard(Item, Mixin_language):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self._language = "EN"

    def __str__(self):
        return f"{self.name}"

    @property
    def language(self):
        return self._language
