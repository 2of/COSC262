class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Return this point/vector as a string in the form "(x, y)" """
        return "({}, {})".format(self.x, self.y)

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

    def __lt__(self, other):
        """For convenience we define '<' to mean
           "less than with respect to angle", i.e.
           the direction of self is less than the
           direction of other in a CCW sense."""
        area = self.x * other.y - other.x * self.y
        return area > 0
        
        
def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise"""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
	 # May want to throw an exception if area == 0
    return area > 0 

def simple_polygon(points):
    """Return the given list of points ordered so that connecting them in order
       yields a simple polygon"""
       
    # Firstly swap the bottommost (and if necessary leftmost) point to the
    # 0th position in the list. The first line finds the bottommost point,
    # and the next line finds its index, so it can be swapped to the front.
    bottommost = min(points, key=lambda p: (p.y, p.x))
    index = points.index(bottommost)
    points[0], points[index] = points[index], points[0]
    
    # Now just sort the rest by angle from points[0]
    rest = points[1:]
    # **** FIXME by inserting the missing line of code here ****
   # print('in func:')
    
    
    rest = sorted(rest, key=lambda x: points[0] - x)
    
    
    #print(rest)
    
    
    
    return [points[0]] + rest
    
    
    
    
def graham_scan(points_):
    '''docstrings are a thing of evil'''
    if not points_:
        return ''
    points = simple_polygon(points_)
    stack = points[0:3]

    for i in range(3, len(points)):
        while not is_ccw(stack[-2], stack[-1], points[i]):
            stack.pop()
        stack.append(points[i])
    return stack    
    