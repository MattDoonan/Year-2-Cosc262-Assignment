from math import inf


def adjacency_list(graph_str):
    """ajacent"""
    new = graph_str.splitlines()
    final = []
    undi = False
    for i in range(len(new)):
        line = new[i].split()
        if i == 0:
            if line[0] == "U":
                undi = True
            for x in range(int(line[1])):
                final.append([])
        elif len(line) == 2:
            target = final[int(line[0])]
            target.append((int(line[1]),None))
            if undi == True:
                target = final[int(line[1])]
                target.append((int(line[0]),None))                
        else:
            target = final[int(line[0])]
            target.append((int(line[1]),(int(line[2]))))   
            if undi == True:
                target = final[int(line[1])]
                target.append((int(line[0]),(int(line[2]))))                   
    return final



def min_capacity(city_map, depot_position):
    adj = adjacency_list(city_map)
    parent, distance = dijkstra(adj, depot_position)
    num = -1
    for i in range(len(distance)):
        if distance[i] > num and distance[i] != inf:
            num = distance[i]
    num *= 3
    result = (num * 100) / 75
    return int(result)
    
    
def next_vertex(in_tree, distance):
    save = 0
    num = sum(distance)
    for i in range(len(in_tree)):
        if in_tree[i] is False:
            if num >= distance[i]:
                save = i
                num = distance[i]
    return save


def dijkstra(adj_list, start):
    n = len(adj_list)
    in_tree = [False for i in range(n)]
    distance = [inf for i in range(n)]
    parent = [None for i in range(n)]
    distance[start] = 0
    while any(y != True for y in in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v,weight in adj_list[u]:
            if in_tree[v] == False and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return parent, distance
  
#Example

city_map = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(min_capacity(city_map, 0))
print(min_capacity(city_map, 1))
print(min_capacity(city_map, 2))
print(min_capacity(city_map, 3))
