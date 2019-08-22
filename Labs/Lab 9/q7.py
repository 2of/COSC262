class Vec:
    """A simple vector in 2D. Also use for points (position vector)"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        return self.dot(self)
        
        
def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise or degenerate"""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
	 # May want to throw an exception if area == 0
    return area > 0 
    
    
def is_strictly_convex(vertices):
    """Return True iff the given vertices define a strictly convex polygon
       with all vertices in counter-clockwise order. The function returns
       false if there are fewer than 3 vertices or if any interior angle is
       less than 180 degrees or the vertices are not in counter-clockwise
       order
    """
    if len(vertices) < 3:
        return False
    for i in range(len(vertices)):
        a = vertices[i]
        b = vertices[(i + 1) % len(vertices)]
        c = vertices[(i + 2) % len(vertices)]
        if not is_ccw(a,b,c):
            return False
    return True
