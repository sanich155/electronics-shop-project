"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import random


def test_Item():

    apple = Item('apple', 55, 70)
    eggs = Item('eggs', 150, 500)

    assert apple.name == 'apple'
    assert apple.price == 55
    assert apple.quantity == 70
    assert apple.calculate_total_price() == 70 * 55
    assert type(random.choice(Item.all)) == Item
    assert len(Item.all) == 2
    apple.apply_discount()
    assert apple.price == 55 * 0.85
