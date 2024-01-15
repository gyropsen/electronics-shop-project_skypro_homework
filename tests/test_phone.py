import pytest

from src.phone import Phone

from src.item import Item


@pytest.fixture
def get_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1


@pytest.fixture
def get_item():
    item1 = Item("Смартфон", 10000, 20)
    return item1


def test_phone(get_phone):
    assert str(get_phone) == 'iPhone 14'
    assert repr(get_phone) == "Phone('iPhone 14', 120000, 5, 2)"
    assert get_phone.number_of_sim == 2


def test__add__(get_item, get_phone):
    assert get_item + get_phone == 25
    assert get_phone + get_phone == 10
