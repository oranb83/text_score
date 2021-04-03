from collections import OrderedDict

from src.string_score import PrefixStringScore
from src.string_score import SuffixStringScore


class TestPrefixStringScore:
    def test_update_substring_score(self):
        # Arrange
        text = 'abcdabcd'
        substring = 'xxabc'
        actual = PrefixStringScore(text)
        expected = OrderedDict({'c': 2, 'bc': 1, 'abc': 0})

        # Act
        actual.update_substring_score(substring)

        # Assert
        assert expected == actual.mapper


class TestSuffixStringScore:
    def test_update_substring_score(self):
        # Arrange
        text = 'abcdabeavbccd'
        substring = 'abcxx'
        actual = SuffixStringScore(text)
        expected = OrderedDict({'a': 7, 'ab': 4, 'abc': 0})

        # Act
        actual.update_substring_score(substring)

        # Assert
        assert expected == actual.mapper
