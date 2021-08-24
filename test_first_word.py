import pytest

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    import re
    m = re.search(r"\w+([']\w*)?", text)
    return m.group(0) if m is not None else ''


def test_first_word():
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"


def test_negative():
    assert first_word("") == ""