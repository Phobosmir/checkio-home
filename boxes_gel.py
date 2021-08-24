import itertools
from typing import List, Tuple
MAX_W = 400
MAX_V = 600

boxes = [(4, 51), (90, 49), (16, 80), (84, 64), (43, 14), (29, 2), (68, 91), (3, 57), (22, 53), (32, 84), (43, 59), (15, 84), (90, 19), (55, 73), (41, 41), (54, 31), (92, 77), (64, 81), (61, 20), (2, 31)]


def calc_sizes(boxes):
    sum_w = sum([box[0] for box in boxes])
    sum_v = sum([box[1] for box in boxes])
    print(f'Weight: {sum_w} Volume: {sum_v}')
    print(f'Left W:  {MAX_W-sum_w} Left V: {MAX_V-sum_v}')
    return MAX_W-sum_w, MAX_V-sum_v


def result(boxes: List[Tuple], max_, index):
    boxes.sort(key=lambda box: box[index])

    print(boxes)

    in_box, out_box = [], []
    sum = 0
    for i, value in enumerate(boxes):
        if sum + value[index] <= max_:
            in_box.append(value)
            sum += value[index]
        else:
            out_box.append(value)
    return in_box, out_box


boxes_ext = [(W, V, W*W/(MAX_W*MAX_V)) for W,V in boxes ]
#boxes.sort(key=lambda box: box[0]*box[0]/MAX_M/MAX_V)


result(boxes_ext, MAX)




"""
print(boxes)
def calc_sizes(boxes):
    print(f'Weight: {sum([box[0] for box in boxes])} Volume: {sum([box[1] for box in boxes])}')

print(boxes)


boxes2 = [box[0]/box[1] for box in boxes]
print(boxes2)
print(sorted(boxes2))
print('...')
boxes.sort(key= lambda box: box[1]/box[0])
print(boxes)
"""
