import pytest

from src.input import Input


class TestInput:
    @pytest.mark.parametrize('input_value,min_size,max_size,expected', [
        (123, 1, 5, False),
        ('ABC', 1, 5, False),
        ('a+bc', 1, 5, False),
        ('ab c', 1, 5, False),
        ('ab c', 1, 5, False),
        ('abAc', 1, 5, False),
        ('', 1, 5, False),
        ('abcdef', 1, 5, False),
        ('ab', 3, 5, False),
        ('abcdef', 1, 6, True)
    ])
    def test_is_valid(self, input_value, min_size, max_size, expected):
        # Arrange
        value = Input(input_value)

        # Act
        actual = value.is_valid(min_size, max_size)

        # Assert
        assert expected == actual
