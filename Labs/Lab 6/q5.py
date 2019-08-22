from math import floor

def fractional_knapsack(capacity, items):
    class item():
        ''' just because tuples are annoying AF to work with'''
        def __init__(self, name, value, size):
            self.name = name
            self.value = value
            self.size = size
            self.weighted_val = value/size
            self.whats_left = 0

    def get_values(items):
        each = []
        for i in items: 
            each.append(item(i[0],i[1],i[2]))
        return each
