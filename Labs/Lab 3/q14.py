import copy

def adjacency_matrix(graph_str):

    data = graph_str.split()
    
    nodes = int(data[1])
    directed = (data[0] == "D")
    del data [:3]
    edges = int(len(data)) / 3
  #  nodes = len ( data)/3
    matrix = [[float('Inf') for x in range(nodes)] for x in range (nodes)]

    for zero in range(nodes):
        matrix[zero][zero] = 0
    
    for i in range(int(edges)):

        from_ = int(data[i*3])
        to_ = int(data[i*3 + 1])
        matrix[from_][to_] = int(data [i*3+2])
        

        if not directed: 
            matrix[to_][from_] = int ( data [i*3+2])

    #print("THE MATRIX: " , matrix)
    return(matrix)




def floyd(inwards_): 
    data = copy.deepcopy(inwards_)
    nodes = len(data)
    
    out = [[float('Inf') for j in range(nodes)] for i in range(nodes)]


 
    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):

                if data[i][j] > data[i][k] + data[k][j]:
                    data[i][j] = data[i][k] + data[k][j]

    return data