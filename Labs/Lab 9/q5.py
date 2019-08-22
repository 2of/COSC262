class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
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

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
        

def is_on_segment(p, a, b):
    """True iff p lies on the line segment from a to b"""
    v1 = a - p
    v2 = b - p
    area = v1.x * v2.y - v1.y * v2.x # Two times area of triangle pab.
    if area == 0:
        seg_len_sq = (a - p).lensq()
        seg_len_sq1 = (b - a).lensq()
        seg_len_sq2 = (b - p).lensq()
        seg_len_sq3 = (b - a).lensq()
       # print(seg_len_sq, a.lensq(),p.lensq(),b.lensq())

       # print(p.dot(a) <= a.dot(b) and p.dot(b) <= a.dot(b))

        if seg_len_sq <= seg_len_sq1 and seg_len_sq2 <= seg_len_sq1:  # ** FIXME **
            return True
    return False
