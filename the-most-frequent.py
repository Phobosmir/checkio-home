"""
ZH-HANS RU JA English
You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.

Input: a list of strings.

Output: a string.

Example:

most_frequent([
    'a', 'b', 'c',
    'a', 'b',
    'a'
]) == 'a'
most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
"""


def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    res = {}
    for d in data:
        res[d] = res.get(d, 0) + 1
    return max(res, key=lambda x: res[x])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))

    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')