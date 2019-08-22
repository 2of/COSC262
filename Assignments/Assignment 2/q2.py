def longest_common_substring(s1, s2): 
    ''' returns the assignment question friends'''
    def build_table(s1, s2):
        '''construct bottom up table'''
        num_cols = len(s1)+1
        num_rows = len(s2)+1
        grid = [[-1 for i in range(num_cols)]for j in range(num_rows)]
        for row in range(num_rows):
            for column in range(num_cols):
                if row == 0 or column == 0:
                    grid[row][column] = 0
                    continue
                if s2[row-1] == s1[column-1]:
                    grid[row][column] = grid[row-1][column-1]+1
                    continue
                else: 
                    grid[row][column] = max(grid[row][column-1], grid[row-1][column])
        return grid


    def iterative_backtrack(grid):
        '''iterative because recursive implementation is nasty '''
        i, j = len(grid)-1, len(grid[0])-1 #offset for 1-origin
        seq = ''
        while (i*j != 0):
        #    print(i,j)
            if i == 0 or j == 0:
                return seq[::-1]
            elif s2[i-1] == s1[j-1]:
                seq += s1[j-1]
                i -= 1
                j -= 1
            else: 
                if grid[i-1][j] > grid[i][j-1]: 
                    i -= 1
                else:
                    j -= 1      
        return (seq[::-1])  
        
    return (iterative_backtrack(build_table(s1, s2)))