#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_letters is ascii_lowercase + ascii_uppercase

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # clean text before passing it to palindrome function
    parsed_text = text.lower().strip()

    return is_palindrome_iterative(parsed_text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    if len(text) == 0 or len(text) == 1:
        return True
    elif len(text) > 1:
        first_pos = 0
        last_pos = -1

        # If the string has an even number of characters
        if len(text) % 2 == 0:
            for index, value in enumerate(text):
                # Check the first position and last position
                if text[first_pos] == text[last_pos]:
                    return True
                else:
                    first_pos += 1
                    last_pos -= 1
        # If the string has an odd number of characters
        if len(text) % 2 == 1:
            for index, value in enumerate(text):
                # Check the first position and last position
                if text[first_pos] == text[last_pos]:
                    return True
                else:
                    first_pos += 1
                    last_pos -= 1
    return False
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
