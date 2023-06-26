"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

def test_init():
    exp = Item("name", 1, 2)
    assert exp.name == "name"
    assert exp.price == 1
    assert exp.quantity == 2

def test_calculate_total_price():
    exp = Item("name", 1, 2)
    assert exp.calculate_total_price() == 2

def test_apply_discount():
    exp = Item("name", 1, 2)
    assert exp.pay_rate * exp.price == 1