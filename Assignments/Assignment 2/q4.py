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
            a, i, j = get_min(grid, i, j, lefts, rights)
            output.append(a)
        return output[::-1]
    return (backtrack(bottom_up(lefts, rights)))