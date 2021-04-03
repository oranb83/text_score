# Substring score calculation
from abc import ABC, abstractmethod
from collections import OrderedDict

NOT_FOUND = -1


class BaseStringScore(ABC):
    """
    This class get's a string score and return the first or last occurence of
    the matching index.
    """
    def __init__(self, text):
        """
        @type text: str
        @param text: lowercase string [a-z]
        """
        self.text = text
        self.mapper = OrderedDict()

    def _get_substring_index(self, substring, reverse):
        """
        Get substring index in text.

        @type substring: str
        @param substring: lowercase string [a-z]
        @type reverse: bool
        @param reverse: False for getting the first index,
                        True for getting the last index
        @rtype: int or None
        @return: if substring is a part of string return it's index,
                 otherwise return None
        """
        index = self.text.find(substring) if not reverse else self.text.rfind(substring)

        return index if index != NOT_FOUND else None

    @abstractmethod
    def update_substring_score(self, substring):
        """
        Update substring score in mapper.

        The last inserted item has the highest score.
        The score will match the amount of items in the mapper key and it's
        value will match either the first or last index depands on the reverse
        flag.

        @type substring: str
        @param substring: lowercase string [a-z]
        @raises NotImplementedError: must be implemented in child class
        """
        raise NotImplementedError


"""
Note: although it's easy the merge the two PrefixString and SuffixString
      classes, I think it's best to split the two because:
      1. It simplifies the code
      2. It makes it more readable
      3. It's easier to test
      4. It's easier to make logical changes that are not bound between the two
         classes
      5. With TDD it just doesn't feels right since I want to test small units
"""
class PrefixStringScore(BaseStringScore):
    """
    PrefixString class will get it's substring score into the mapper.
    """
    def update_substring_score(self, substring):
        for i in range(1, len(substring) + 1):
            sub = substring[-i:]
            index = self._get_substring_index(sub, False)
            if index is None:
                break

            self.mapper[sub] = index


class SuffixStringScore(BaseStringScore):
    """
    SuffixString class will get it's substring score into the mapper.
    """
    def update_substring_score(self, substring):
        for i in range(1, len(substring) + 1):
            sub = substring[:i]
            index = self._get_substring_index(sub, True)
            if index is None:
                break

            self.mapper[sub] = index
