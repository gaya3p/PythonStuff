c, f = 4, 5
fs = {
   (1, 2): 10,
   (1, 3): 24,
   (2, 3): 2,
   (2, 4): 15,
   (3, 4): 7
}

import heapq


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


example_graph = {
    'U': {'V': 10, 'W': 24},
    'V': {'U': 10, 'X': 15, 'W': 2},
    'W': {'V': 2, 'U': 24, 'X': 7},
    'X': {'V': 15, 'W': 7},
    # 'Y': {'X': 1, 'W': 1, 'Z': 1},
    # 'Z': {'W': 5, 'Y': 1},
}

print(calculate_distances(example_graph, 'X'))

# => {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}

# from itertools import permutations
# c, f = list(map(int, input().split()))

# fs = {
#    (1, 2): 10,
#    (1, 3): 24,
#    (2, 3): 2,
#    (2, 4): 15,
#    (3, 4): 7
# }
# # for i in range(f):
# #     x, y, p = list(map(int, input().split()))
# #     fs[(x, y)] = p


# l = [i for i in range(1, c+1)]
# perms = list(permutations(l))

# min_c = 0
# costs = []

# for path in perms:
#     cost = 0
#     f = True

#     for i in range(c-1):
#         t = (path[i], path[i+1])
#         t2 = (path[i+1], path[i])
        
#         if t in fs:
#             cost += fs[t]

#         elif t2 in fs:
#             cost += fs[t2]

#         else:
#             f = False
#             break
            
#     else:
#         if f:
#             costs.append(cost)
        
# # minimum cost
# print(min(costs))
        

