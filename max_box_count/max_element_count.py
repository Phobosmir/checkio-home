from typing import List, Tuple

boxes = [(4, 51), (90, 49), (16, 80), (84, 64), (43, 14), (29, 2), (68, 91), (3, 57), (22, 53), (32, 84), (43, 59),
         (15, 84), (90, 19), (55, 73), (41, 41), (54, 31), (92, 77), (64, 81), (61, 20), (2, 31)]

current_weight = 908
current_volume = 1061


def calc_sizes(boxes):
    sum_m = sum([box[0] for box in boxes])
    sum_v = sum([box[1] for box in boxes])
    print(f'Weight: {sum_m} Volume: {sum_v}')
    print(f'Left W: {MAX_M - sum_m} Left V: {MAX_V - sum_v}')
    return MAX_M - sum_m, MAX_V - sum_v


def result(boxes: List[Tuple]):
    boxes.sort(key=lambda box: box[0]*box[1])
    print(boxes)

    res = []
    sum_m, sum_v = 0, 0
    for box in boxes:
        if sum_m + box[0] <= MAX_M and sum_v + box[1] <= MAX_V:
            sum_m += box[0]
            sum_v += box[1]
            res.append(box)

    return res



MAX_M = 400
MAX_V = 600

print(boxes)
print(f'MAX_W: {MAX_M} MAX_V: {MAX_V}')
MV = MAX_V * MAX_M
print(f'M*V: {MV}')

print('SUM of boxes MV: ', sum([b[0]*b[1] for b in boxes]))


calc_sizes(boxes)
boxes = result(boxes)
print(boxes)
calc_sizes(boxes)
# apply alogor. on the rest with the new max values.
