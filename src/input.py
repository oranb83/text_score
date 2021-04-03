# Process user input
import re
import logging

logger = logging.getLogger(__name__)


class Input:
    """
    This class process user input and validates it based on predefined rules.
    """
    def __init__(self, input_value):
        """
        @type input_value: str
        @param input_value: valid input is a lowercase string [a-z]
        """
        self.input = input_value

    def is_valid(self, min_size=1, max_size=50):
        """
        Validate input.

        @type min_size: int
        @param min_size: min input length defaulted to 0
        @type max_size: int
        @param max_size: max input length defaulted to inf which means no limit
        """
        is_valid_value = True
        if not self._is_string():
            logger.error('%s is not a string', self.input)
            is_valid_value = False
        elif not self._is_lowercase():
            logger.error('%s is not lowercase [a-z]', self.input)
            is_valid_value = False
        elif not self._is_valid_length(min_size, max_size):
            logger.error('%s length is invalid: min_size=%d and max_size=%d',
                         self.input, min_size, max_size)
            is_valid_value = False

        return is_valid_value

    def _is_string(self):
        """
        Check if input is string.

        @rtype: bool
        @return: True if string, otherwise False
        """
        return isinstance(self.input, str)

    def _is_lowercase(self):
        """
        Check if input is lowercase english alphabet.

        @rtype: bool
        @return: True if lowercase english alphabet, otherwise False
        """
        return re.match('^[a-z]*$', self.input) is not None

    def _is_valid_length(self, min_size=0, max_size=float('inf')):
        """
        Check if input has valid length.

        @type min_size: int
        @param min_size: defaulted to 0
        @type max_size: int
        @param max_size: defaulted to infinity which means no limit
        @rtype: bool
        @return: True if lowercase english alphabet, otherwise False
        """
        return len(self.input) >= min_size and len(self.input) <= max_size
