def get_min(grid, i, j, s1, s2):
    '''Docstrings are annoying in these lil quizzes
    
    Honestly pythons modular list access thing is the most frustarting thing
    in this entire damned cours e : ( '''
    if j >= 1:
        s1str = s1[j-1] 
    else:
        s1str = ''
    if i >= 1:
        s2str = s2[i-1]
    else:
        s2str = ''
    min_ = float('Inf')
    ni, nj = i, j
    tuple_back = ()
    if s1str == s2str:
        return [("T", s1str, s2str), i-1, j-1]
    if grid[i][j-1] < min_:
        min_ = grid[i][j-1]
        tuple_back = ("D", s1str, '')
        ni = i
        nj = j-1
  
        
    if grid[i-1][j] < min_:
        min_ = grid[i-1][j]
        tuple_back = ("I", '', s2str)
        ni = i-1
        nj = j
    
    if grid[i-1][j-1] < min_:
        
        min_ = grid[i-1][j-1]
        tuple_back = ("S", s1str, s2str)
        ni = i -1 
        nj = j - 1
    
    return [tuple_back, ni, nj]
        
    
    
    


def bottom_up(lefts, rights): 
    '''yeet'''
    grid = [[-1 for i in range(len(lefts)+1)] for j in range(len(rights)+1)]
    for i in range(len(rights)+1):
        for j in range(len(lefts)+1):
            if i == 0 and j == 0:
                grid[i][j] = 0 
            elif j == 0:
                grid[i][j] = i
            elif i == 0:
                grid[i][j] = j 
            elif (lefts[j-1] == rights[i-1]):
                grid[i][j] = grid[i-1][j-1]               
            else: 
                grid[i][j] = 1 + (min(grid[i-1][j], grid[i][j-1], grid[i-1][j-1]))
    return grid

    
def checkbase(s1, s2):
    '''I dislike the pylint prick'''
    if len(s1) + len(s2) == 0:
        return ''
    if len(s1) == 0:
        return [('I', '', s2[0])]
    return [('D', s1[0], '')]
    
def line_edits(s1, s2):
    '''Comprises a docstring to appease cosc peeps'''
    # initial recursive implementation:
    lefts, rights = str.splitlines(s1), str.splitlines(s2)
    if s1 == "" or s2 == "":
        return checkbase(lefts, rights)
    
    def backtrack(grid):
        ''' :-( '''
        j, i, output = len(grid[0])-1, len(grid)-1, []
        while i != 0:    
            oldi,oldj = i,j
            a, i, j = get_min(grid, i, j, lefts, rights)
            
            
            if (a[0]) == 'S':
                lcs = longest_common_substring(a[1],a[2])
                lcsbkp = lcs [:]
                line1 = str_dif(lcs,a[1])
                line2 = str_dif(lcsbkp,a[2])
                b1 =  line1
                b2 = line2
                oldi,oldj = i,j
                a = ("S",b1,b2)
                
                
                
            
            
            output.append(a)
        return output[::-1]
    return (backtrack(bottom_up(lefts, rights)))

def str_dif(lcs, string_):
    s = list(string_)
    for c in range(len(s)):
        if lcs and lcs[0] == s[c]:
            del lcs[0]
        else:
            s[c] = f'[[{s[c]}]]'
            


    return ''.join(s)

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
        return list(seq[::-1])  
        
    return (iterative_backtrack(build_table(s1, s2)))


import sys