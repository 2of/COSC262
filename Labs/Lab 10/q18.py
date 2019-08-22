#the tractability here is bad fam
try:
    from sortedcontainersx import SortedList
except ModuleNotFoundError:
    # sortedcontainers not installed.
    import bisect
    class SortedList:
        """An approximation to the SortedList class that 
           uses a normal list that's kept sorted.
           Inefficient but good enough for this exercise. 
        """
        def __init__(self, items=None, key=lambda x: x):
            """Initialiser creates a sorted list with a specified
               key function used for sorting.
            """
            if items is None:
                self.items = []
            else:
                self.items = items[:]
            self.key = key
            self.items.sort(key=key)
            
        def __getitem__(self, index):
            """Index into the list to get an item"""
            return self.items[index]
        
        def __setitem__(self, index, value):
            """Update an items in the list"""
            self.items[index] = value
            
        def add(self, item):
            """Add item to list, keeping it ordered. Item goes
               after any existing items equal to it (using the key).
            """
            self.items.insert(self.bisect_right(item), item)
            
        def remove(self, item):
            """Remove the first occurrence of item"""
            self.items.remove(item)
            
        def pop(self, index=-1):
            """Pop and return the index-th item in the list"""
            return self.items.pop(index)
        
        def bisect_left(self, value, lo=0, hi=None):
            """Locate the insertion point in the list to insert value,
               such that the new value comes before any existing equal values.
               This implementation is O(n) but this isn't meant to be
               an efficient implementation. It's pretty sad that the bisect
               module doesn't support a key function, though.
            """
            return bisect.bisect_left([self.key(item) for item in self.items], self.key(value))
                
        def bisect_right(self, value, lo=0, hi=None):
            """Locate the insertion point in the list to insert value,
               such that the new value comes after any existing equal values.
               See previous method for various disclaimers.
            """
            return bisect.bisect_right([self.key(item) for item in self.items], self.key(value))            
    
class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)
    
    def __repr__(self):
        return f"Vec({self.x}, {self.y})"
    
    
def slow_solution(points):
    soln = (points[0], points[1])
    d = (points[0] - points[1]).lensq()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = (points[i] - points[j]).lensq()
            if dist < d:
                soln = (points[i], points[j])
                d = dist
    return soln


def closest_pair(points_in):
    """Return the two closest points in the given point set.
       Precondition: points has a length >= 2.
       The return value is a tuple of two points of type Vec, sorted by
       their x values and then, if they are equal, their y values.
    """
    points = sorted(points_in, key=lambda p: (p.x, p.y))  # Point list acts as event queue
    solution = (points[0], points[1])      # Current best point pair
    d = (points[1] - points[0]).lensq()    # Current best point-pair distance

    # Construct the frontier list, which is kept sorted by y
    # **** Insert some code here to create the initial frontier list with
    # **** the first two elements of the sorted point list.

    frontier = SortedList(points[0:3], key = lambda p: (p.x, p.y))
    # Now sweep the line across the point set, starting the points[2]
    i = 2

    while d > 0 and i < len(points):
        p = points[i]

        for point in frontier:
            if p.x - point.x > d:
                frontier.remove(point)    
        for point in frontier: 
            comp = (p-point).lensq() 
            if  comp < d and comp != 0:
                d = comp
                solution = (p,point)
        frontier.add(p)
        i += 1
        

    return tuple(sorted(solution, key=lambda p: (p.x, p.y)))

