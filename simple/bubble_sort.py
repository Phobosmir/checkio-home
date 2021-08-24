import random

def bubble_sort(l: list):
    list_size = len(l)
    for cur_i in range(list_size-1):
        for j in range(cur_i+1, list_size):
            if l[cur_i] > l[j]:
                    l[cur_i], l[j] = l[j], l[cur_i]
    return l

def bubble_sort2(l: list):
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                is_sorted = False

    return l



def bubble_sort_on_iterators(iterable):
    r = []
    first_iter = iter(iterable)
    second_iter = iter(iterable)

    for x in iterable:
        r.append(x)




for _ in range(10):
    t = (list(range(100)))
    random.shuffle(t)
    assert bubble_sort2(t.copy()) == sorted(t)
