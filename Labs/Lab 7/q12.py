class Item:
    """An item to (maybe) put in a knapsack"""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
    def __repr__(self):
        return (f"{self.value} , {self.weight}\n")
        
def max_value(items, capacity):
    """The maximum value achievable with a given list of items and a given
       knapsack capacity."""
       
       # *** IMPLEMENT ME ***
    #items = items.sort(key = lambda x: x.weight)
    
    items = (sorted(items,key = lambda x: x.weight)) #sort them fam
    grid = [[0 for i in range(capacity+1)] for i in range(len(items)+1)]
      
    for i in range(len(grid)):
        for w in range(len(grid[0])):
            if i ==0 or w == 0:
                grid[i][w] = 0
            elif items[i-1].weight <= w:
                grid[i][w] = max(items[i-1].value + grid[i-1][w-items[i-1].weight], grid[i-1][w])
            else: 
                grid[i][w] = grid[i-1][w]
                
    return grid[i][w]