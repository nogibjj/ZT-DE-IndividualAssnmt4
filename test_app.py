from app import random_fruit


def test_random_fruit():
    assert random_fruit() in ["watermelon", "banana", "blueberry"]
