import pytest
from Models.shopping_cart import ShoppingCart


class TestShoppingCart:
    @pytest.fixture
    def cart(self) -> ShoppingCart:
        return ShoppingCart()

    def test_init_creates_empty_items(self, cart: ShoppingCart) -> None:
        assert cart.items == []

    def test_add_new_item(self, cart: ShoppingCart) -> None:
        cart.add_item("Laptop", 1200.0, 1)
        assert len(cart.items) == 1
        assert cart.items[0] == {
            "name": "Laptop",
            "price": 1200.0,
            "quantity": 1,
        }

    def test_add_existing_item_sums_quantity_and_updates_price(self, cart: ShoppingCart) -> None:
        cart.add_item("Mouse", 25.0, 2)
        cart.add_item("Mouse", 30.0, 3)

        assert len(cart.items) == 1
        assert cart.items[0] == {
            "name": "Mouse",
            "price": 30.0,
            "quantity": 5,
        }

    def test_remove_existing_item(self, cart: ShoppingCart) -> None:
        cart.add_item("Keyboard", 75.0, 1)
        cart.add_item("Monitor", 300.0, 2)

        cart.remove_item("Keyboard")

        assert len(cart.items) == 1
        assert cart.items[0]["name"] == "Monitor"

    def test_remove_nonexistent_item_does_nothing(self, cart: ShoppingCart) -> None:
        cart.add_item("Keyboard", 75.0, 1)
        cart.remove_item("Headphones")

        assert len(cart.items) == 1
        assert cart.items[0]["name"] == "Keyboard"