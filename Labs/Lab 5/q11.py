

def radix_sort(vals, d):

    for i  in range(d):
 #       print("sort char {}".format(i))
        b = lambda x: (x % 10**(i+1))
        
        vals = sorted(vals, key = b)
        
       
    return vals
