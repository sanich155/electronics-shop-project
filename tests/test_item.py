"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import random
from settings import ITEMS_PATH


def test_Item():

    apple = Item('apple', 55, 70)
    eggs = Item('eggs', 150, 500)

# Homework-1
    assert apple.name == 'apple'
    assert apple.price == 55
    assert apple.quantity == 70
    assert apple.calculate_total_price() == 70 * 55
    assert type(random.choice(Item.all)) == Item
    assert len(Item.all) == 2
    apple.apply_discount()
    assert apple.price == 55 * 0.85

# Homework-2
    apple.name = 'The biggest apple in the world'
    assert apple.name == 'The bigges'
    apple.name = 'BigApple'
    assert apple.name == 'BigApple'

    Item.instantiate_from_csv(ITEMS_PATH)  # создание объектов из данных файла
    assert len(Item.all) == 7  # в файле 5 записей с данными по товарам

    assert eggs.string_to_number('12345') == 12345
    assert eggs.string_to_number('3.0') == 3
    assert eggs.string_to_number('5.5') == 5
