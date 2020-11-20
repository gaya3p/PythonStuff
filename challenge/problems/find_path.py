''' Floyd–Warshall algorithm '''
v, e = 4, 5
a = [[-1 for _ in range(v)] for _ in range(v)]
for i in range(v):
    for j in range(v):
        if i == j:
            a[i][j] = 0
        else:
            a[i][j] = -1

inp = [[1, 2, 10],
    [1, 3, 24],
    [2, 3, 2],
    [2, 4, 15],
    [3, 4, 7]
]

for i in range(e):
    x, y, l = inp[i]
    a[x-1][y-1] = l
    a[y-1][x-1] = l

# print(a)

for k in range(v):
    for i in range(v):
        for j in range(v):
            
            # if i!=j and (a[i][j]>a[i][k] + a[k][j] or a[i][j] == -1) and a[i][k]>-1 and a[k][j]>-1:
            if i!=j and a[i][k]>-1 and a[k][j]>-1:
                # print(i, j, k, a[i][j])
                if (a[i][j]>a[i][k] + a[k][j] or a[i][j] == -1):
                    a[i][j] = a[i][k] + a[k][j]

max = 0
for i in range(v):
    for j in range(v):
        if a[i][j] > max:
            max = a[i][j]

# print(max)

''' Dijkstra's Algorith '''
import heapq

def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    print(distances)

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        # print(pq)
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        # print(current_distance, distances[current_vertex])
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            # print(neighbor, weight, current_vertex)
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

print(calculate_distances(example_graph, 'U'))


def dijkstra(graph, start, goal):
    shortest_distance = {}
    track_predecessor = {}
    unseen_nodes = graph
    path = []
    infinity = 99999999

    for node in unseen_nodes:
        shortest_distance[node] = infinity 
    shortest_distance[start] = 0

    while unseen_nodes:

        min_distance_node = None

        for node in unseen_nodes:
            if min_distance_node is None:
                min_distance_node = start
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        # print(min_distance_node)
        path_options = graph[min_distance_node].items()

        for child_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node

        unseen_nodes.pop(min_distance_node)

    current_node = goal

    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = track_predecessor[current_node]

        except KeyError:
            print('Path is not reachable')
            break
    
    path.insert(0, start)

    if shortest_distance[goal] != infinity:
        print('ans:', shortest_distance[goal])
        print(path)

dijkstra(example_graph, 'U', 'W')

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
        

