def which_walkways(campus_map):
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

    data = adjacency_list(campus_map)
    def prim(data,start):

        def NEXT_VERTEX(in_tree, distance):
            if True not in in_tree: 
                return 0
            a = min(distance)
            mval = float('Inf')
            at = 0

            for i in range(0,len(in_tree)):
             #   print(i, distance[i])
                if distance[i] < mval and (not in_tree[i]): 

                    mval = distance[i]
                    at = i
            if mval == float('Inf'):
                return distance.index(float('Inf'))

          #  print("TRUE{}".format(mval))
            return at




           # print(a)

        n = len(data)
        in_tree = [False for x in range(n)]
        distance = [float('Inf') for x in range(n)]
        parent = [None for x in range (n)]
        distance[start] = 0
        #in_tree[start] = True
        u = start
       
       
        while False in in_tree:
       #     time.sleep(1)
            
       #     print("U I S {}".format(u))
      #      print(in_tree, distance)
            for v,weight in data[u]:
              #  print(v,weight,in_tree[v],(not in_tree[u]), (weight < distance[v]))
                if (not in_tree[v] and weight < distance[v]):
                    distance[v] = weight
                    parent[v] = u
            u = NEXT_VERTEX(in_tree,distance)
            in_tree[u] = True
            
            
        return (parent) 


       
    
    a =  (prim(data,0))

    result = []
    for i in range(len(a)):
        if a[i] is not None:
            result.append(tuple(sorted((a[i],i))))

    
   # print("{} -> {}".format(a, result))

  #  for i in range(len(a)):
   #     if a[i] is not None:
     #       result.append((a[i],i))
#

    return result

