"""
Nicola regularly inspects the local networks for security issues. He uses a smart and aggressive program which takes control of computers on the network. This program attacks all connected computers simultaneously, then uses the captured computers for further attacks. Nicola started the virus program in the first computer and took note of the time it took to completely capture the network. We can help him improve his process by modeling and improving his inspections.
We are given information about the connections in the network and the security level for each computer. Security level is the time (in minutes) that is required for the virus to capture a machine. Capture time is not related to the number of infected computers attacking the machine. Infection start from the 0th computer (which is already infected). Connections in the network are undirected. Security levels are not equal to zero (except infected).
Information about a network is represented as a matrix NxN size, where N is a number of computers. If ith computer connected with jth computer, then matrix[i][j] == matrix[j][i] == 1, else 0. Security levels are placed in the main matrix diagonal, so matrix[i][i] is the security level for the ith computer.
attack

You should calculate how much time is required to capture the whole network in minutes.

Input: Network information as a list of lists with integers.
Output: The total time of taken to capture the network as an integer.

Example:

capture([[0, 1, 0, 1, 0, 1],
         [1, 8, 1, 0, 0, 0],
         [0, 1, 2, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 3, 1],
         [1, 0, 1, 0, 1, 2]]) == 8
capture([[0, 1, 0, 1, 0, 1],
         [1, 1, 1, 0, 0, 0],
         [0, 1, 2, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 3, 1],
         [1, 0, 1, 0, 1, 2]]) == 4
capture([[0, 1, 1],
         [1, 9, 1],
         [1, 1, 9]]) == 9

How it is used: This concept shows how to model and examine various network configurations. The idea does not only apply to computer networks however, it can also be a model for the spread of disease or dissemination of rumors.

Precondition:

3 ≤ len(matrix) ≤ 10
matrix[0][0] == 0
all(len(row) == len(matrix[0]) for row in matrix)
all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix)))
all(0 < matrix[i][i] < 10 for i in range(1, len(matrix)))
all(0 ≤ matrix[i][j] ≤ 1 for i in range(len(matrix)) for j in range(len(matrix)) if i != j)
How to improve this mission? https://github.com/Bryukh-Checkio-Tasks/checkio-mission-network-attack.git { 10 }
"""

class NetworkHost:
    def __init__(self, security_level, host_index):
        self.security_level = security_level
        self.host_index = host_index
        self.connections = set()




def capture2(matrix):
    network = {cur_host: NetworkHost(host_info[cur_host], cur_host) for cur_host, host_info in enumerate(matrix)}

    for host_index, host_info in enumerate(matrix):
        cur_host = network[host_index]
        for connected_host_index, is_connected in enumerate(host_info):
            if connected_host_index == host_index:
                continue
            if is_connected:
                cur_host.connections.add(network[connected_host_index])

    res = 0
    infected_hosts = [network[0]]
    visited_hosts = set()


    while infected_hosts:
        cur_host = infected_hosts.pop()
        res += cur_host.security_level
        visited_hosts.add(cur_host)

        for h in cur_host.connections:
            if h not in visited_hosts:
                infected_hosts.append(h)
    return res


from heapq import heappush, heappop
class InfectionTimeline:
    def __init__(self):
        self.heap = []

    def add_infected_host(self, security_level, host_index, connected_hosts):
        heappush(self.heap, (security_level, host_index, connected_hosts))

    def get_next_infected_host(self):
        return heappop(self.heap)

def capture(matrix):
    uninfected_hosts = set(range(0, len(matrix)))

    infection_timeline = InfectionTimeline()
    infection_timeline.add_infected_host(0, 0, matrix[0])

    cur_time = 0
    while uninfected_hosts:
        cur_time, cur_host_index, connected_hosts = infection_timeline.get_next_infected_host()
        if cur_host_index not in uninfected_hosts:
            continue
        for host_index, is_connected in enumerate(connected_hosts):
            if cur_host_index == host_index:
                continue
            if is_connected:
                connected_host_security_level = matrix[host_index][host_index]
                infection_timeline.add_infected_host(cur_time + connected_host_security_level, host_index, matrix[host_index])
        uninfected_hosts.remove(cur_host_index)
    return cur_time

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"

    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 1, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"

    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 9, 1, 0, 0, 0],
                    [0, 1, 1, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 9, "Base example"