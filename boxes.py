import itertools
from typing import List, Tuple

boxes = [(4, 51), (90, 49), (16, 80), (84, 64), (43, 14), (29, 2), (68, 91), (3, 57), (22, 53), (32, 84), (43, 59), (15, 84), (90, 19), (55, 73), (41, 41), (54, 31), (92, 77), (64, 81), (61, 20), (2, 31)]

current_weight = 908
current_volume = 1061


def calc_sizes(boxes):
    print(f'Weight: {sum([box[0] for box in boxes])} Volume: {sum([box[1] for box in boxes])}')


max_weight_box = max([box[0] for box in boxes])
#print('Max W:', max_weight_box)
max_volume_box = max([box[1] for box in boxes])
#print('Max V:', max_volume_box)

print(boxes)

MAX_V = 400
MAX_W = 600

boxes.sort(key=lambda box: box[0]*box[1]/MAX_V/ MAX_W)
r1 =itertools.accumulate([box[0] for box in boxes])
r2 =itertools.accumulate([box[1] for box in boxes])
print(boxes)
print(list(zip(r1, r2)))

[(1,5), (1,1), (1,1), (1,2)]
