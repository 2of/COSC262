def computation_order(adapters_info):
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
                    to_add = to_add = (int(data[i*jumpamount]),None)         
                    lst[int(data[i*jumpamount+1])].append(to_add)

        return lst    


    def bfs(data):
        ''' two hour long nasty rewrite thnx stackoverflow gods'''
        node_edges = [0]*(len(data)) 

        for top in range(0,len(data)): 
            for nextboi in data[top]:
                node_edges[nextboi[0]] += 1
        output,visits = [],0

        queue = [] 
        for i in range(len(data)):      # praised documentation
            if node_edges[i] == 0: 
                queue.append(i) 


        while queue: 
            active = queue.pop(0) 
            output.append(active) 
            for i in data[active]:
                if i != None:
                    node_edges[i[0]] -= 1 #decrement nodes on element.

                if node_edges[i[0]] == 0:
                    queue.append(i[0])
            visits += 1
  

        if visits != len(data):  # we have seen all nodes, if we havent then a node isnt 
                        # touched by the main tree but is not a unique node. Dear god this was trouble!
            return None
        else : 
            a = output[::-1]
        return a




    data = adjacency_list(adapters_info)


    return (bfs(data))