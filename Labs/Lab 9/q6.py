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
    """True iff triangle abc is counter-clockwise"""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
	 # May want to throw an exception if area == 0
    return area > 0 


def intersecting(a, b, c, d):
    """True iff line segment ab intersects cd"""
    # 1. Check if points c & d are on opposite sides of the line ab
    condition1 = is_ccw(a, d, b) == is_ccw(a, b, c)
    
    #2. Check if points a & b are on opposite sides of the line cd
    condition2 = is_ccw(c,a,d) != is_ccw(c,b,d)
    return condition1 and condition2