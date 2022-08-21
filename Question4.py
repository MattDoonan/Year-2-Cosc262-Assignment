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



def which_segments(city_map):
    adj = adjacency_list(city_map)
    n = len(adj)
    parent, distance = prim(adj, 0)
    final = []
    for i in range(len(parent)):
        if parent[i] != None:
            want = sorted((parent[i],i))
            final.append((want[0],want[1]))
    return final

def prim(adj, s):
    n = len(adj)
    in_tree = [False for i in range(n)]
    distance = [inf for i in range(n)]
    parent = [None for i in range(n)]
    distance[s] = 0
    while all(in_tree) is not True:
        u = next_vertex(in_tree,distance)
        in_tree[u] = True
        for v, weight in adj[u]:
            if in_tree[v] == False and weight < distance[v]:
                distance[v] = weight
                parent[v] = u
    return parent, distance


def next_vertex(in_tree, distance):
    save = 0
    num = sum(distance)
    for i in range(len(in_tree)):
        if in_tree[i] is False:
            if num >= distance[i]:
                save = i
                num = distance[i]
    return save

#Example
city_map = """\
U 3 W
0 1 1
2 1 2
2 0 4
"""

print(sorted(which_segments(city_map)))
