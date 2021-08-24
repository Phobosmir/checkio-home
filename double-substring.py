"""
This is the third mission of the series, and it’s the only one where you have to return not a substring but a substring length.
You need to find a substring that repeats more than once in a given string. This reiteration shouldn't have overlaps.
For example, in a string "abcab" the longest substring that repeats more than once is "ab", so the answer should be 2 (length of "ab")

Input: String.

Output: Int.
"""


def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    max_sub_len = 0
    for start_idx in range(0, len(line)-1):
        for end_idx in range(start_idx + 1, len(line)):
            if end_idx - start_idx > len(line)/2:
                continue
            sub = line[start_idx:end_idx]
            if line.count(sub) > 1:
                max_sub_len = len(sub) if len(sub) > max_sub_len else max_sub_len
    return max_sub_len

"""
import re
def double_substring(line):

    return max(map(len,re.findall(r'(?=([a-zA-Z].*).*\1)',line))) if re.findall(r'(?=([a-zA-Z].*).*\1)',line) else 0
    
def double_substring(line):
    l = len(line)
    # max possible length of substring
    ll = l // 2
    
    # brute force solution
    for i in range(ll, 0, -1):
        for j in range(l-i):
            if line[j:j+i] in line[j+i:]:
                return i
    else:
        return 0    
    
"""

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aa') == 1
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')
