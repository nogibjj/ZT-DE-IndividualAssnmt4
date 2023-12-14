from app import random_fruit


def test_random_fruit():
    assert "watermelon" or "banana" or "blueberry" in random_fruit()
