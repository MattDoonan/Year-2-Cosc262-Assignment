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

def build_order(dependencies):
    adj = adjacency_list(dependencies)
    found, order = dfs_tree(adj, 0)    
    for i in range(len(found)):
        if found[i] == 'U':
            dfsLoop(adj, i, found, order)
    order.reverse()
    return order
            


def dfs_tree(adj_list, start):
    n = len(adj_list)
    s = ['U' for i in range(n)]
    s[start] = 'D'
    order = []
    dfsLoop(adj_list, start, s, order)
    return s, order
    
def dfsLoop(adj_list, start, s, order):
    for i in adj_list[start]:
        if s[i[0]] == "U":
            s[i[0]] = "D"
            dfsLoop(adj_list, i[0], s, order)
    s[start] = "P"
    order.append(start)
    
#Example
dependencies = """\
D 3
"""
# any permutation of 0, 1, 2 is valid in this case.
solution = build_order(dependencies)
if solution is None:
    print("Wrong answer!")
else:
    print(sorted(solution))
