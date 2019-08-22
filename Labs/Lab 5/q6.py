def key_positions(seq,key):

    j = (max(seq, key = key))
    k = key(j)
    c = [0 for i in range(0,k+1)]
  #  print(k,len(c))
    j = max(seq)

    for a in seq: 
        c[key(a)] = c[key(a)]+1
    sum = 0

    for i in range(0,k+1): 
        c[i],sum = sum,sum+c[i]
    return c

