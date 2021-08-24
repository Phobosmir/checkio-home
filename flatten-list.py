"""
Nicola likes to categorize all sorts of things. He categorized a series of numbers and as the result of his efforts, a simple sequence of numbers became a deeply-nested list. Sophia and Stephan don't really understand his organization and need to figure out what it all means. They need your help to understand Nikolas crazy list.

There is a list which contains integers or other nested lists which may contain yet more lists and integers which then… you get the idea. You should put all of the integer values into one flat list. The order should be as it was in the original list with string representation from left to right.

We need to hide this program from Nikola by keeping it small and easy to hide. Because of this, your code should be shorter than 140 characters (with whitespaces).

Input data: A nested list with integers.

Output data: The one-dimensional list with integers.

Example:

flat_list([1, 2, 3]) == [1, 2, 3]
flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]
1
2
3
4
How it is used: This concept is useful for parsing and analyzing files with complex structures and the task challenges your creativity in writing short code.

Precondition: 0 ≤ |array| ≤ 100
∀ x ∈ array : -232 < x < 232 or x is a list
depth < 10

How to improve this mission? https://github.com/Bryukh-Checkio-Tasks/checkio-task-all-in-row.git { 12 }
"""

def flat_list_works(array):
    r = []
    for x in array:
        if isinstance(x, list):
            r.extend(flat_list(x))
        else:
            r.append(x)
    return r

def flat_list_works2(array):
    def g(val):
        for v in val:
            if isinstance(v, list):
                # for i in v:
                #    yield i
                yield from g(v)
            else:
                yield v
    return list(g(array))


def flat_list(array):
    r = []
    for v in array:
        r += flat_list(v) if isinstance(v, list) else [v]
    return r

def flat_list_other(array):
    return [elem for arr in array for elem in flat_list(arr)] if isinstance(array, list) else [array]


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')