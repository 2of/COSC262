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
        
def is_ccw(p0, p1, p2):
    """True if triangle p0, p1, p2 has vertices in counter-clockwise order"""
    return (p1 - p0) < (p2 - p0)
    
        
def gift_wrap(points):
    """ Returns points on convex hull in CCW using the Gift Wrap algorithm"""
    # Get the bottom-most (and left-most if necessary) point as points[0]
    assert len(points) >= 3
    for i, p in enumerate(points):
        if (p.y, p.x) < (points[0].y, points[0].x):
            points[i], points[0] = points[0], p

    hull = []
    point_on_hull = points[0]
    
    # Loop, adding one edge at a time, until hull is about to be closed.
    while len(hull) < 2 or point_on_hull is not points[0]:
        hull.append(point_on_hull)
        candidate = None
        # Loop through all points, looking for the one that is "rightmost"
        # looking from point_on_hull
        for p in points:
            if p is point_on_hull:
                continue
            if candidate == None or not is_ccw(candidate, p, point_on_hull):
                candidate = p
        point_on_hull = candidate

    return hull
