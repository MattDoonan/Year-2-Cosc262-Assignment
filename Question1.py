from collections import deque


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

def format_sequence(converters_info, source_format, destination_format):
    """format"""
    adj = adjacency_list(converters_info)
    if source_format > len(adj):
        return "No solution!"
    parent = (bfs_tree(adj, source_format))
    if parent[destination_format] == None:
        if source_format == destination_format:
            return [source_format]
        return "No solution!"
    i = destination_format
    path = []
    while i != source_format:
        path.append(i)
        i = parent[i]
    path.append(i)
    return [ele for ele in reversed(path)]
        


def bfs_tree(adj_list, start):
    n = len(adj_list)
    state = ['U' for i in range(n)]
    p = [None for i in range(n)]
    q = deque()
    state[start] = 'D'
    q.append(start)
    return bfsLoop(adj_list, q, state, p)

def bfsLoop(adj_list, q, state, p):
    while len(q) > 0:
        u = q.popleft()
        for i in adj_list[u]:
            if state[i[0]] == 'U':
                state[i[0]] = 'D'
                p[i[0]] = u
                q.append(i[0])
        state[u] = 'P'
    return p
