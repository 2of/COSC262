def permutations(s):
    out = []
    lst = list(s)
    
    def add_out(string):
        out.append(tuple(string))


    def permute(length_des,point, string = ()):
        if len(string) == length_des:
            add_out( string)
        else:
            for i in range(point, length_des):

                lst[point], lst[i] = lst[i], lst[point] 
                permute(length_des,point+1,string + ((lst[point]),))

                lst[i], lst[point] = lst[point], lst[i] 





    permute(len(s),0)

                

    return out
