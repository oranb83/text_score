from src.input import Input
from src.text_score import TextScore


def validate_user_input(user_input):
    """
    If user input is valid return it, otherwise exit.
    """
    if not Input(user_input).is_valid():
        print('Exiting program due to illegal input value!')
        exit(1)

    return user_input


def main():
    print('Please enter strings:')
    string_text = validate_user_input(input('text: '))
    prefix_string = validate_user_input(input('prefixString: '))
    suffix_string = validate_user_input(input('suffixString: '))

    return TextScore(string_text, prefix_string, suffix_string).get_highscore_smallest_substring()


if __name__ == '__main__':
    matching_substring = main()
    print('The substring of text with the highest textScore is:', matching_substring)
