import pytest
from utils.utils import calculate_discount, is_even, get_full_name


# 5 тестів для calculate_discount

def test_calculate_discount_20_percent():
    assert calculate_discount(100, 20) == 80.0


def test_calculate_discount_50_percent():
    assert calculate_discount(250, 50) == 125.0


def test_calculate_discount_0_percent():
    assert calculate_discount(500, 0) == 500.0


def test_calculate_discount_zero_price():
    assert calculate_discount(0, 15) == 0.0


def test_calculate_discount_float_values():
    assert calculate_discount(99.99, 10) == pytest.approx(89.991)


# 5 тестів для is_even

def test_is_even_positive_even():
    assert is_even(4) is True


def test_is_even_positive_odd():
    assert is_even(7) is False


def test_is_even_negative_even():
    assert is_even(-10) is True


def test_is_even_negative_odd():
    assert is_even(-3) is False


def test_is_even_zero():
    assert is_even(0) is True


# 5 тестів для get_full_name

def test_get_full_name_standard():
    assert get_full_name("Тарас", "Шевченко") == "Тарас Шевченко"


def test_get_full_name_short():
    assert get_full_name("Ян", "Лі") == "Ян Лі"


def test_get_full_name_long():
    assert get_full_name("Олександр", "Костянтинопільський") == "Олександр Костянтинопільський"


def test_get_full_name_single_chars():
    assert get_full_name("А", "Б") == "А Б"


def test_get_full_name_with_hyphen():
    assert get_full_name("Анна-Марія", "Ковальчук-Мельник") == "Анна-Марія Ковальчук-Мельник"