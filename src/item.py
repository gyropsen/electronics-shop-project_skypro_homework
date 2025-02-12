import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self._name}', "
                f"{self.price}, {self.quantity})")

    def __str__(self):
        return f"{self._name}"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity

    @property
    def name(self):
        """
        Геттер name
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Сеттер name
        """
        if len(name) <= 10:
            self._name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_coast = self.quantity * self.price
        return total_coast

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path="../src/items.csv"):
        """
        Создает экземпляры класса из файла
        """
        try:
            cls.all.clear()
            with open(path, "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile, delimiter=",")
                for row in reader:
                    cls(str(row['name']), int(row['price']), int(row['quantity']))

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        else:
            if len(cls.all) != 5:
                raise InstantiateCSVError("Файл item.csv поврежден")

    @staticmethod
    def string_to_number(number_string):
        """
        Проверка вхождения числа в строку
        """
        for number in number_string:
            if number.isdigit():
                return int(number)


class InstantiateCSVError(Exception):
    pass
