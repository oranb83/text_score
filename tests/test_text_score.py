import pytest

from src.text_score import TextScore


class TestTextScore:
    @pytest.mark.parametrize('text,prefix_string,suffix_string,expected', [
        ('abcdefg', 'fg', 'ab', 'ab'),
        ('abcabdef', 'de', 'bd', 'bd'),
        ('abcabdef', 'cxab', 'bdf', 'abcabd'),
        ('abcabdef', 'cxab', 'abf', 'ab'),
        ('abcabdef', 'cxab', 'aexx', 'a'),
        ('abcabdef', 'xxab', 'ab', 'ab'),
        ('axbcabdefxef', 'bc', 'ef', 'bcabdef'),
        ('abcdef', 'ab', 'ab', 'ab'),
        ('abcdef', 'ef', 'ab', 'ab'),
        ('engineneg', 'ravene', 'neginkgo', 'eneg'),
        ('engine', 'ravene', 'gin', 'engin'),
        ('eginenxx', 'e', 'gin', 'egin'),
        ('eginenxx', 'en', 'ginbra', 'gin'),
        ('enxginxenxenginxxzgin', 'xzcen', 'ginbra', 'enxgin'),
        ('ab', 'b', 'a', 'a'),
        ('ab', 'a', 'b', 'ab'),
        ('nothing', 'bruno', 'ingenious', 'nothing'),
        ('engine', 'raven', 'ginko', 'engin'),
        ('engine', 'raven', '', 'en'),
        ('engine', '', 'ginko', 'gin'),
        ('engine', 'gin', 'i', 'gi'),
        ('engine', 'gin', 'n', 'gin'),
        ('enxgine', 'gin', 'x', 'gin'),
        ('enexeeginee', 'abe', 'iba', 'eegi'),
    ])
    def test_get_highscore_smallest_substring(
        self, text, prefix_string, suffix_string, expected):
        # Arrange
        text_score = TextScore(text, prefix_string, suffix_string)

        # Act
        actual = text_score.get_highscore_smallest_substring()

        # Assert
        assert expected == actual

    def test_get_highscore_smallest_substring_no_match(self):
        # Arrange
        text_score = TextScore('engine', 'foo', 'bar')

        # Act & Assert
        pytest.raises(ValueError, text_score.get_highscore_smallest_substring)
