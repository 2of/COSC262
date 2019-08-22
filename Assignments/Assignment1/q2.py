def arrangement(adapters_info):
    def adjacency_list(graph_str):
      #  print("THE STRING LENGTH IS {}".format(len(graph_str)))
        
        data = graph_str.split()
     #   print("DATA IS {} LEN {}".format(data,len(data)))
        if len(data) == 2:
            return [[] for x in range( int(data[1]))]


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

    def bfs_tree(adj_list,start,visits):
     #   print(adj_list, " IN BFS CINTS")
        nodes = len(adj_list)
        parents = [None for x in range(nodes)]
        queue = []
        inthis = []
        queue.append(start)
     
      
     
        while queue:
            active = queue[0]
            if active not in inthis:
                inthis.append(active)
            del queue[0]
            for i in adj_list[active]:
                if visits[i[0]] == "U":
                    visits[i[0]] = "F"
                    queue.append(i[0])
                    parents[i[0]] = active
        parents[start] = None 
        visits[start] = "F"
        return (inthis)




    data = adjacency_list(adapters_info)
    visits = ["U" for x in range(len(data))]
    results = []
    while ("U" in visits):
        if data:
          #  time.sleep(1)
            a = bfs_tree(data,visits.index("U"),visits)
           # print(a,visits)
        results.append(a)
    return results
