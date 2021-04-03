# Text score calculation
import re

from src.string_score import PrefixStringScore, SuffixStringScore


class TextScore:
    """
    This class calculates the text score and decides which text substring to
    return. The returned substring will be of the highest score. In case of a
    match it will return the lowest lexicographic substring.
    """
    def __init__(self, text, prefix_string, suffix_string):
        self.text = text
        self.prefix_string = prefix_string
        self.suffix_string = suffix_string

    def get_highscore_smallest_substring(self):
        """
        Get the smallest substring with the highest text score.

        @raises ValueError: in case there is no match to text
        @rtype: str
        @return: substring
        """
        prefix_string_score = PrefixStringScore(self.text)
        prefix_string_score.update_substring_score(self.prefix_string)
        suffix_string_score = SuffixStringScore(self.text)
        suffix_string_score.update_substring_score(self.suffix_string)

        if len(prefix_string_score.mapper) == 0 and len(suffix_string_score.mapper) == 0:
            raise ValueError('prefixString or suffixString must match text')
        if len(prefix_string_score.mapper) == 0:
            return suffix_string_score.mapper.popitem()[0]
        if len(suffix_string_score.mapper) == 0:
            return prefix_string_score.mapper.popitem()[0]

        max_score = 0
        smallest_substring = None
        for prefix_string, prefix_index in reversed(prefix_string_score.mapper.items()):
            for suffix_string, suffix_index in reversed(suffix_string_score.mapper.items()):
                if smallest_substring is None:
                    smallest_substring = self.text[prefix_index : suffix_index + len(suffix_string)]

                # TODO: change this to a switch case (Python doesn't have it built in)
                if prefix_index <= suffix_index:
                    max_score, smallest_substring = self._get_score_prefix_index_lte_suffix_index(
                        prefix_string, suffix_string, max_score, smallest_substring)
                elif len(prefix_string) == len(suffix_string) and len(prefix_string) > max_score:
                    max_score = len(prefix_string)
                    smallest_substring = min(prefix_string, suffix_string)
                elif len(prefix_string) > len(suffix_string) and len(prefix_string) >= max_score:
                    max_score, smallest_substring = self._update_score_prefix_index_gt_suffix_index(
                        prefix_string, max_score, smallest_substring)
                elif len(prefix_string) < len(suffix_string) and len(suffix_string) >= max_score:
                    max_score, smallest_substring = self._update_score_prefix_index_gt_suffix_index(
                        suffix_string, max_score, smallest_substring)

        return smallest_substring

    @staticmethod
    def _update_score_prefix_index_gt_suffix_index(string, max_score, smallest_substring):
        """
        Calculate the smallest substring and it's score in case prefix_index > suffix_index.

        @note: func suffix gt represents greater than
        @type string: str
        @param string: substring of prefix string or suffix string
        @type smallest_substring: str
        @param smallest_substring: smallest substring so far
        @type max_score: int
        @param max_score: represents the smallest substring high score
        @rtype: tuple<str, str>
        @return: max_score and smallest_substring
        """
        if len(string) == max_score:
            smallest_substring = min(string, smallest_substring)
        else:
            max_score = len(string)
            smallest_substring = string

        return max_score, smallest_substring

    def _get_score_prefix_index_lte_suffix_index(self, prefix_string, suffix_string, max_score,
                                                 smallest_substring):
        """
        Calculate the smallest substring and it's score in case prefix_index <= suffix_index.

        @note: func suffix lte represents less than equal
        @type prefix_string: str
        @param prefix_string: substring of prefix string
        @type suffix_string: str
        @param suffix_string: substring of suffix string
        @type max_score: int
        @param max_score: represents the smallest substring high score
        @type smallest_substring: str
        @param smallest_substring: smallest substring so far
        @rtype: tuple<str, str>
        @return: max_score and smallest_substring
        """
        score = len(prefix_string) + len(suffix_string)
        if score < max_score:
            return max_score, smallest_substring

        max_score = score
        for p in re.finditer(prefix_string, self.text):
            for s in re.finditer(suffix_string, self.text):
                if p.span()[0] > s.span()[0]:
                    break

                substring = self.text[p.span()[0] : s.span()[1]]
                smallest_substring = min(substring, smallest_substring)

        return max_score, smallest_substring
