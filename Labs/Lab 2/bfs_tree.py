def bfs_tree(adj_list,start):
    nodes = len(adj_list)
    parents = [None for x in range(nodes)]
    queue = []
    visits = ["U" for x in range(nodes)]



    queue.append(start)


    while queue: 
        active = queue[0]
        del queue[0]
        for i in adj_list[active]:
            if visits[i[0]] == "U":
                visits[i[0]] = "F"
                queue.append(i[0])
                parents[i[0]] = active
    parents[start] = None #Just a wee problem but thats okay fix
    return parents