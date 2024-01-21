from src.keyboard import Keyboard
import pytest


@pytest.fixture
def get_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard(get_keyboard):
    assert str(get_keyboard) == "Dark Project KD87A"

    assert str(get_keyboard.language) == "EN"

    get_keyboard.change_lang()
    assert str(get_keyboard.language) == "RU"

    # Сделали EN -> RU -> EN
    get_keyboard.change_lang()
    assert str(get_keyboard.language) == "EN"
