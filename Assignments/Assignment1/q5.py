
import copy
def maximum_energy(campus_map,pos):
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





    
    def dijkstras(data, start):
        timeout = 0
        if len(data[start]) == 0:
            return [0]


        def NEXT_VERTEX(in_tree, dist):
            if True not in in_tree: 
                return 0
            a = min(dist)
            mval = float('Inf')
            at = 0
            for i in range(0,len(in_tree)):
               # print(i)
                if dist[i] < mval and (not in_tree[i]): 
                    mval = dist[i]
                    at = i
            if mval == float('Inf'):
                try:
                    return dist.index(float('Inf'))
                except:
                    return None
            return at



        u = start
        in_tree[start] = True
        dist[start] = 0
        while False in in_tree:
            in_tree[u] = True
            for i in range(len(data[u])):
                v = i 
                neighbour = data[u][v][0]
                alt = dist[u] + data[u][v][1]
                if alt < dist[neighbour]:
                    dist[neighbour] = alt
                    parent[neighbour] = u 
            u = NEXT_VERTEX(in_tree,dist)
            if not u:
               timeout += 1
            if timeout > 30:
                return dist
        return dist








        
    data = adjacency_list(campus_map)

    nodes = len(data)
    dist = [float('Inf') for x in range(nodes)]
    parent = [None for x in range(nodes)]
    in_tree = [False for x in range(nodes)]

    result = (dijkstras(data,pos))


    
   
    maximum = 0
   # print(result)
    for b in range(len(result)):
        if result[b] != float('Inf') and maximum < result[b]:
            maximum = result[b]
    return maximum*2 
