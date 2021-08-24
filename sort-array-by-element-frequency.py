"""
Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.

Input: Iterable

Output: Iterable

Example:

frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
1
2
Precondition: elements can be ints or strings

The mission was taken from Python CCPS 109 Fall 2018. It's being taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen

How to improve this mission? https://github.com/oduvan/checkio-mission-frequency-sort { 6 }
"""
import itertools

def frequency_sort_own(items):
    item_freq = {item: count for count,group in itertools.groupby(items, key=items.count) for item in group}
    return [k for k in sorted(item_freq, key=item_freq.get, reverse=True) for _ in range(item_freq[k])]


from collections import Counter

def frequency_sort(items):
    c = dict(Counter(items).most_common())
    l = [x for x in c for i in range(c.get(x))]
    return l

def frequency_sort(items):
    return sorted(items, key =lambda x: (-items.count(x), items.index(x)))



if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]

    assert list(frequency_sort([4,6,2,2,2,6,4,4,4])) == [4,4,4,4,2,2,2,6,6]
    print("Coding complete? Click 'Check' to earn cool rewards!")