def calculate_discount(price: float, discount: float) -> float:
    """Обчислює ціну після застосування знижки у відсотках"""
    return price - (price * discount / 100)


def is_even(number: int) -> bool:
    """Перевіряє, чи є ціле число парним"""
    return number % 2 == 0


def get_full_name(first_name: str, last_name: str) -> str:
    """Повертає повне ім'я та прізвище одним рядком через пробіл"""
    return f"{first_name} {last_name}"