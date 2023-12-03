import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all = []

    def __init__(self, __name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param __name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = __name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path):
        with open(path, 'r', encoding='latin1') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cls(row['name'], float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(num_str):
        return int(float(num_str))
