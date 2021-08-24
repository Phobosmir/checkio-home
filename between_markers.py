"""
You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:

The initial and final markers are always different.
If there is no initial marker, then the first character should be considered the beginning of a string.
If there is no final marker, then the last character should be considered the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker comes before the initial marker, then return an empty string.
Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string.

Example:

between_markers('What is >apple<', '>', '<') == 'apple'
between_markers('No[/b] hi', '[b]', '[/b]') == 'No'
1
2
How it is used: for parsing texts

Precondition: can't be more than one final marker and can't be more than one initial
"""
"""
def between_markers(text: str, begin: str, end: str) -> str:

    # your code here
    start = text.find(begin) + len(begin) if text.find(begin) >= 0 else 0
    stop = text.find(end) if text.find(end) >= 0 else None
    return text[start:stop]


def between_markers(text: str, begin: str, end: str) -> str:

    _, _, text = text.rpartition(begin)
    text, _, _ = text.partition(end)
    return text
"""

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    if begin == end:
        raise Exception('"Begin" should be different with "end"')

    idx_begin=text.find(begin)
    idx_end=text.find(end)

    def _both_begin_and_end_are_in_text():
        return idx_end != -1 and idx_begin != -1

    def _both_begin_and_end_are_not_in_text():
        return idx_end == -1 and idx_begin == -1

    if _both_begin_and_end_are_in_text():
        if idx_end > idx_begin:
            return text[(idx_begin + len(begin)):idx_end]
        elif idx_end < idx_begin:
            return ''
    elif _both_begin_and_end_are_not_in_text():
        return text[:]
    else:
        if idx_begin == -1:
            return text[:idx_end]
        if idx_end == -1 :
            return text[idx_begin + len(begin):]



if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>abc', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
