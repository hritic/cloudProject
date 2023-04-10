import networkx as nx
import heapq

# Define a DAG
G = nx.DiGraph()
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B', 'D')
G.add_edge('C', 'D')

# Define job durations
durations = {
    'A': 4,
    'B': 2,
    'C': 3,
    'D': 1
}

# Define scheduling algorithms
def sjf(G, durations):
    """
    Shortest Job First scheduling algorithm
    """
    ready = list(nx.topological_sort(G))
    schedule = []
    heap = []
    time = 0
    while ready or heap:
        if not heap:
            node = ready.pop(0)
            heapq.heappush(heap, (durations[node], node))
        duration, node = heapq.heappop(heap)
        schedule.append((node, time))
        time += duration
        for successor in G.successors(node):
            if successor not in [x[1] for x in heap]:
                heap.append((durations[successor], successor))
        heapq.heapify(heap)
    return schedule

def fifo(G, durations):
    """
    First In First Out scheduling algorithm
    """
    ready = list(nx.topological_sort(G))
    schedule = []
    time = 0
    for node in ready:
        schedule.append((node, time))
        time += durations[node]
    return schedule

# Print results
print("Shortest Job First schedule:")
print(sjf(G, durations))
print("First In First Out schedule:")
print(fifo(G, durations))