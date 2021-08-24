"""
Write a function that finds the longest palindromic substring of a given string. Try to be as efficient as possible!

If you find more than one substring you should return the one which is closer to the beginning.

Input: A text as a string.

Output: The longest palindromic substring.

Examples:

longestPalindromic("artrartrt") == "rtrartr"
longestPalindromic("abacada") == "aba"
longestPalindromic("aaaa") == "aaaa"

1
2
3
4
Precondition: 1 ≤ |text| ≤ 20
The text contains only ASCII characters.
"""

import pytest

def longest_palindromic_own(text):
    if text == text[::-1]:
        return text
    res = ''

    for start in range(0, len(text)):
        for stop in range(len(text), start, -1):
            if abs(start-stop) <= len(res):
                continue
            s1 = text[start:stop]
            s2 = text[stop-1:start-len(text)-1:-1]
            if s1 == s2:
                res = s1

    return res


def longest_palindromic(text):
    def is_palindromic(txt):  # functions
        return txt == txt[::-1]

    if is_palindromic(text):
        return text

    n = len(text)
    for w in range(n, 2, -1):
        for i in range(n - w):
            if is_palindromic(text[i:i + w]):
                return text[i:i + w]
    return text[0]

def test_one_letter():
    assert longest_palindromic("a") == 'a'

def test_two_letters():
    assert longest_palindromic("ab") == 'a'

def test_three_letters():
    assert longest_palindromic("aba") == "aba"

def test_whole_word():
    assert longest_palindromic("abcba") == "abcba"

def test_with_ord_letters():
    assert longest_palindromic("caa") == "aa"

def test_with_gabarge_at_begin():
    assert longest_palindromic("123abcba") == "abcba"


def test_with_gabarge_at_end():
    assert longest_palindromic("abcba123") == "abcba"


def test_at_the_middle():
    assert longest_palindromic("456abcba123") == "abcba"


def test_the_logest():
    assert longest_palindromic("abcbaabcdcba") == "abcdcba", "The logest"


def test_the_logest_separated():
    assert longest_palindromic("abcba123abcdcba") == "abcdcba", "The logest"


def test_the_first():
    assert longest_palindromic("1abacada2") == "aba"


def test_only_one():
    assert longest_palindromic("abcde") == "a"

import sys
if __name__ == '__main__':
    pytest.main(sys.argv)