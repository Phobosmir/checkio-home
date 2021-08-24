"""
And now, finally, the mission's objective. Given a room's size and a list of PIR sensors mounted on the room's ceiling and looking down on the floor, your task is to determine whether the floor area is completely into the sensors coverage area (return True) or not (return False). The bottom left corner of the rectangle matches the origin point O, the top right corner is defined by W and H. Each sensor is defined by its mounting point (coordinates xi and yi) and its range (Ri).

Input: Two arguments:

the first is a list containing a room's top right corner coordinates,all are integers [W, H]
the second is a list containing sensors info, all are integers [[xi, yi, Ri], [xi+1, yi+1, Ri+1], ....., [xn, yn, Rn]]
Output: True or False.


"""

import itertools
import math


def get_y_for_circle(x, center_x, center_y, radius):
    if abs(x - center_x) > radius:
        raise ValueError()
    y = math.sqrt(radius ** 2 - (center_x - x) ** 2)
    return (math.ceil(center_y - y), math.floor(center_y + y))


def is_covered(room, sensors):
    covered_by_sensor = set()
    for sensor_x, sensor_y, sensor_r in sensors:
        covered_by_sensor.update(points_covered_by_sensor(sensor_x, sensor_y, sensor_r))

    room_points = itertools.product(range(room[0] + 1), range(room[1] + 1))
    for p in room_points:
        if p not in covered_by_sensor:
            return False

    return True


def points_covered_by_sensor(center_x, center_y, radius):
    r = set()
    for x in range(center_x - radius, center_x + radius + 1):
        y_min, y_max = get_y_for_circle(x, center_x, center_y, radius)
        for y in range(y_min, y_max + 1):
            r.add((x, y))
    return r
    # return [(x, get_y_for_circle(center_x, radius)) for x in range(radius - center_x, radius + center_x + 1)]
    # return zip(range(radius - center_x, radius + center_x + 1), get_y_for_circle(center_x, radius))


if __name__ == '__main__':
    print("Example:")
    print(is_covered([200, 150], [[100, 75, 130]]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_covered([200, 150], [[100, 75, 130]]) == True
    assert is_covered([200, 150], [[50, 75, 100], [150, 75, 100]]) == True
    assert is_covered([200, 150], [[50, 75, 100], [150, 25, 50], [150, 125, 50]]) == False
    assert is_covered([200, 150], [[100, 75, 100], [0, 40, 60], [0, 110, 60], [200, 40, 60], [200, 110, 60]]) == True
    assert is_covered([200, 150], [[100, 75, 100], [0, 40, 50], [0, 110, 50], [200, 40, 50], [200, 110, 50]]) == False
    assert is_covered([200, 150], [[100, 75, 110], [105, 75, 110]]) == False
    assert is_covered([200, 150], [[100, 75, 110], [105, 75, 20]]) == False
    assert is_covered([3, 1], [[1, 0, 2], [2, 1, 2]]) == True
    assert is_covered([30, 10], [[0, 10, 10], [10, 0, 10], [20, 10, 10], [30, 0, 10]]) == True
    assert is_covered([30, 10], [[0, 10, 8], [10, 0, 7], [20, 10, 9], [30, 0, 10]]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
