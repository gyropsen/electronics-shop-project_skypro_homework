"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def get_items():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    return item1, item2


@pytest.fixture
def get_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1


def test_calculate_total_price(get_items):
    assert get_items[0].calculate_total_price() == 10000 * 20
    assert get_items[1].calculate_total_price() == 20000 * 5


def test_apply_discount(get_items):
    assert 10000 * Item.pay_rate == get_items[0].price
    assert 20000 * Item.pay_rate == get_items[1].price


def test_item_name(get_items):
    assert get_items[0].name == "Смартфон"

    get_items[0].name = "Ноутбук"
    assert get_items[0].name == "Ноутбук"

    get_items[0].name = "Суперсмартфон"
    assert get_items[0].name == "Ноутбук"


def test_instantiate_from_csv(get_items):
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5


def test_string_to_number(get_items):
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr(get_items):
    assert repr(get_items[0]) == "Item('Смартфон', 10000, 20)"
    assert str(get_items[0]) == 'Смартфон'


def test__add__(get_items, get_phone):
    assert get_items[0] + get_phone == 25
