import itertools
from typing import List, Tuple

boxes = [(4, 51), (90, 49), (16, 80), (84, 64), (43, 14), (29, 2), (68, 91), (3, 57), (22, 53), (32, 84), (43, 59), (15, 84), (90, 19), (55, 73), (41, 41), (54, 31), (92, 77), (64, 81), (61, 20), (2, 31)]



def calc_sizes(boxes):
    sum_w = sum([box[0] for box in boxes])
    sum_v = sum([box[1] for box in boxes])
    print(f'Weight: {sum_w} Volume: {sum_v}')
    print(f'Left W:  {MAX_W-sum_w} Left V: {MAX_V-sum_v}')
    return MAX_W-sum_w, MAX_V-sum_v

def brute_force(boxes, max_w, max_v):
    def _is_ok(boxes):
        sum_w = sum([box[0] for box in boxes])
        if sum_w > max_w:
            return False
        sum_v = sum([box[1] for box in boxes])
        if sum_v > max_v:
            return False
        return True

    res = []
    found_len = None

    for element_count in range(len(boxes), 0, -1):
        if found_len and element_count < found_len:
            break

        for m in itertools.combinations(boxes, element_count):
            if _is_ok(m):
                found_len = len(m)
                res.append(list(m))

    return res

MAX_W = 400
MAX_V = 600

results = brute_force(boxes, MAX_W, MAX_V)
print('Answer:')
for r in results:
    r.sort(key=lambda box: box[0])
    print(r)

print('Original:')
print(boxes)

boxes.sort(key=lambda box: box[0]*100/MAX_V/MAX_W + box[1]/MAX_V/MAX_W)
print('Sorted')
print(boxes)

res = []
sum_1, sum_2 = 0, 0
for box in boxes:
    if sum_1 + box[0] > MAX_W:
        break
    if sum_2 + box[1] > MAX_V:
        break
    sum_1 += box[0]
    sum_2 += box[1]
    res.append(box)
res.sort(key=lambda box: box[0])
print(res)
calc_sizes(res)

