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

def bubbles(physical_contact_info):
    """format"""
    adj = adjacency_list(physical_contact_info)
    bubbles = []
    for i in range(len(adj)):
        same = False
        for x in bubbles:
            for y in x:
                if y == i:
                    same = True
        if same is False:
            parent = bfs_tree(adj, i)
            bubbles.append([])
            bubbles[-1].append(i)
            for v in range(len(parent)):
                if parent[v] is not None:
                    bubbles[-1].append(v)
    return bubbles

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
  
 
#Example

physical_contact_info = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
