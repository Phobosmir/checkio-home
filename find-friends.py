"""
Sophia's drones are not soulless and stupid drones; they can make and have friends. In fact, they already are working for the their own social network just for drones! Sophia has received the data about the connections between drones and she wants to know more about relations between them.

We have an array of straight connections between drones. Each connection is represented as a string with two names of friends separated by hyphen. For example: "dr101-mr99" means what the dr101 and mr99 are friends. Your should write a function that allow determine more complex connection between drones. You are given two names also. Try to determine if they are related through common bonds by any depth. For example: if two drones have a common friends or friends who have common friends and so on.

network
Let's look at examples:
scout2 and scout3 have the common friend scout1 so they are related. super and scout2 are related through sscout, scout4 and scout1. But dr101 and sscout are not related.

Input: Three arguments: Information about friends as a tuple of strings; first name as a string; second name as a string.

Output: Are these drones related or not as a boolean.

Example:

check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "scout2", "scout3") == True
check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout") == False

How it is used: This concept will help you find not too obvious connections with the building of bond networks. And how to work social networks.

Precondition: len(network) ≤ 45
if "name1-name2" in network, then "name2-name1" not in network
3 ≤ len(drone_name) ≤ 6
first_name and second_name in network.

How to improve this mission? https://github.com/Bryukh-Checkio-Tasks/checkio-task-find-friends.git { 17 }
"""


class Drone:
    def __init__(self, name):
        self.name = name
        self.friends = set()
    def add_friend(self, friend_name):
        self.friends.add(friend_name)



def check_connection(network, first, second):
    drones = {}
    for pair in network:
        first_in_pair_name, second_in_pair_name = pair.split('-')
        first_drone = drones.get(first_in_pair_name, Drone(first_in_pair_name))
        second_drone = drones.get(second_in_pair_name, Drone(second_in_pair_name))

        drones[first_in_pair_name] = first_drone
        drones[second_in_pair_name] = second_drone

        first_drone.add_friend(second_drone)
        second_drone.add_friend(first_drone)


    unchecked_drones = [drones[first]]
    checked_drone_names = set()

    while unchecked_drones:
        drone = unchecked_drones.pop()
        checked_drone_names.add(drone.name)
        for drone_friend in drone.friends:
            if drone_friend.name == second:
                return True
            if drone_friend.name not in checked_drone_names:
                unchecked_drones.append(drone_friend)
    return False

"""
from itertools import chain


def check_connection(network, first, second):
    visited = {first}
    destinations = {tuple(x.split("-")) for x in network}
    while visited:
        pairs = {x for x in destinations if any(y in x for y in visited)}
        visited = {x for x in set(chain(*pairs)) if x not in visited}
        if second in visited:
            return True
        destinations -= pairs

    return False

from collections import defaultdict

def check_connection(network, first, second):
    network = [n.split('-') for n in network]
    neighbours = defaultdict(set)
    for a, b in network:
        neighbours[a].add(b)
        neighbours[b].add(a)

    to_visit, visited = {first}, set()
    while to_visit:
        current = to_visit.pop()
        if current == second:
            return True
        visited.add(current)
        to_visit.update(neighbours[current] - visited)
    return False


other

def check_connection(network, first, second):
    setlist = []
    for connection in network:
        s = ab = set(connection.split('-'))
        # unify all set related to a, b
        for t in setlist[:]: # we need to use copy
            if t & ab:       # check t include a, b
                s |= t
                setlist.remove(t)
        setlist.append(s)    # only s include a, b
    return any(set([first, second]) <= s for s in setlist)


from itertools import chain

def check_connection(shakehands, me, you):
    hands = {tuple(pair.split('-')) for pair in shakehands}
    amigos = {me}

    while amigos != set():
        pairs = {pair for pair in hands if any(one in pair for one in amigos)}
        amigos = set(chain(*pairs)) - amigos
        if you in amigos: return True
        hands -= pairs

    return False

def check_connection(network, first, second):
    team = {first}
    for _ in network:
        for edge in network:
            pair = set(edge.split('-'))
            if pair & team:
                team |= pair
    return second in team

"""

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
