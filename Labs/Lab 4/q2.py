def all_paths(graph_string, source, destination):
    out = []
    
    def adjacency_list(graph_str):
        data = graph_str.split()
        nodes = int(data[1])
        directed = (data[0]== "D")
        weighted =  (data[2] == "W")
        jumpamount = 2
        del data[:2]

        if weighted:
            jumpamount = 3
            del data[0]
        edges = int(len(data)/jumpamount)
        lst = [[] for x in range(nodes)]
        for i in range(0,edges,1):
            if weighted:
                to_add = (int(data[i*jumpamount+1]),int(data[i*jumpamount+2]))
                lst[int(data[i*jumpamount])].append(to_add)
                if not directed:
                    to_add = (int(data[i*jumpamount]),int(data[i*jumpamount+2]))
                    lst[int(data[i*jumpamount+1])].append(to_add)
            else:
                to_add = (int(data[i*jumpamount+1]),None)
                lst[int(data[i*jumpamount])].append(to_add)
                if not directed:
                    to_add = to_add = (int(data[i*jumpamount]),None)            # PROBLEM IS ON UNDIRECTED LARGE GRAPH
                    lst[int(data[i*jumpamount+1])].append(to_add)
        return lst

    def add_out(string):
        out.append(list(string))



    data = adjacency_list(graph_string)
    current = source
    nodes = len(data)
    visited = [False for x in range(nodes)]
    distance = [0 for x in range(nodes)]
    parent = [None for x in range(nodes)]

    path = []

    def find_path(current):
       #add_out("TESTESTSE")
        #add_out("ASDAS")
        visited[current] = True
        path.append(current)
        if current == destination:
            add_out(path)
        else:
            for i in data[current]:
                if visited[i[0]] == False:
                    find_path(i[0])
        path.pop()
        visited[current] = False



    




    find_path(source)
    return out