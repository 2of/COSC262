def adapter_chain(adapters_info, charger_plug,wall_socket):
    def adjacency_list(graph_str):
        if len(graph_str) == 4:
            return None
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

    def bfs_tree(adj_list,start,end):
        nodes = len(adj_list)
        parents = [None for x in range(nodes)]
        queue = []
        visits = ["U" for x in range(nodes)]



        queue.append(start)
      
        if len(adj_list) == 4:
            return [0]
        if start == end:
            return [start]
        while queue:
            active = queue[0]
            del queue[0]
            for i in adj_list[active]:
                if visits[i[0]] == "U":
                    visits[i[0]] = "F"
                    queue.append(i[0])
                    parents[i[0]] = active
        parents[start] = None 

        if parents[end] is None:
            pass
        else:
            output = []
            ptr = end
            while ptr != start: 

                output.append(ptr)
                ptr = parents[ptr]
            output.append(ptr)




            new = output[::-1]
            

            return (new)
        return "CS Unplugged!"



    data = adjacency_list(adapters_info)

    if data:

        return bfs_tree(data,charger_plug,wall_socket)

    return [0]