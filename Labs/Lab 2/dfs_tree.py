def dfs_tree(adj_list, start) :
    parent = [None for x in range(len(adj_list))]
    stack  = [start]
    states = ["U" for x in range(len(adj_list))]



    
        
    while stack:
       # time.sleep(0.3)
        active = stack[-1]
   #     print("!!{}".format(active),stack,parent,states)
        states[start] = "D"
 
        if "U" not in [states[edge[0]] for edge in adj_list[active]]:
            # stand ded 
            states[active] = "P"
            stack.pop()
        else: 



            for edge in adj_list[active]:
                #print(edge,states[edge[0]], (edge[0] == "U"))
                if states[edge[0]] == 'U':
                    states[edge[0]] = "D"
                    stack.append(edge[0])
                    parent[edge[0]] = active


                    break
    parent[start] = None
    return parent
