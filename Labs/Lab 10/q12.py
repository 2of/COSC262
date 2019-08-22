class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    point_num = 0
    box_calls = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.label = 'P' + str(Vec.point_num)
        Vec.point_num += 1

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)

    def in_box(self, bottom_left, top_right):
        """True iff this point (warning, not a vector!) lies within or on the
           boundary of the given rectangular box area"""
        Vec.box_calls += 1
        return bottom_left.x <= self.x <= top_right.x and bottom_left.y <= self.y <= top_right.y

    def __getitem__(self, axis):
        return self.x if axis == 0 else self.y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)
        
    def __lt__(self, other):
        """Less than operator, for sorting"""
        return (self.x, self.y) < (other.x, other.y)
        
    
class KdTree:
    """A 2D k-d tree"""
    LABEL_POINTS = True
    LABEL_OFFSET_X = 0.25
    LABEL_OFFSET_Y = 0.25    
    def __init__(self, points, depth=0, max_depth=10):
        """Initialiser, given a list of points, each of type Vec, the current
           depth within the tree (0 for the root) and the maximum depth
           allowable for a leaf node.
        """
        if len(points) < 2 or depth >= max_depth: # Ensure at least one point per leaf
            self.is_leaf = True
            self.points = points
        else:
            self.is_leaf = False
            self.axis = depth % 2  # 0 for vertical divider (x-value), 1 for horizontal (y-value)
            points = sorted(points, key=lambda p: p[self.axis])
            halfway = len(points) // 2
            self.coord = points[halfway - 1][self.axis]
            self.leftorbottom = KdTree(points[:halfway], depth + 1, max_depth)
            self.rightortop = KdTree(points[halfway:], depth + 1, max_depth)
            
    def points_in_range(self, query_rectangle):
        """Return a list of all points in the tree 'self' that lie within or
           on the boundary of the given query rectangle, which is defined by
           a pair of points (bottom_left, top_right), both of which are Vecs.
        """
        pass   # Replace me with a full implementation
        # ITS ALWAYS THE LAST FUCKING VALUE JEEPERS CREEPERS COORD AND AXIS? 
    
        result = []
        def add_result(items):
            for item in items:
                a = Vec(item[0],item[1])
                #print('add',item)
                if a.in_box(query_rectangle[0],query_rectangle[1]):
                    result.append(item)
        
        def get_points(node, rect):
            #because NORMAL people just use damned x and y
            if node.is_leaf:
                #print('add mul',node.points)
                add_result(node.points)
            
            else:
                c1 = [rect[0][0],rect[1][0]]
                if node.axis:
                    c1 = [rect[0][1],rect[1][1]]
                
                if c1[0] < node.coord and c1[1] < node.coord:
                   # print('left')
                    return (get_points(node.leftorbottom,rect))
                if c1[0] > node.coord and c1[1] > node.coord:
                    return (get_points(node.rightortop,rect))
                if c1[0] == node.coord:
                    return(get_points(node.leftorbottom,rect),get_points(node.rightortop,rect))
                if c1[0] < node.coord and node.coord < c1[1]:
                    return(get_points(node.leftorbottom,rect),get_points(node.rightortop,rect))
                if node.coord == c1[1]:
                    return(get_points(node.leftorbottom,rect))
        get_points(self, query_rectangle)
        return result        

    
    
    
    def nearest_point(self,p):
        
        
        def get_node_loc(node,point,prev = None):
            
            if node.is_leaf:
               # print('use node',node)
                return node
            else: 
                if node.coord < point[node.axis]:
                    return (get_node_loc(node.leftorbottom,point,node))
                    #print('riught')
                else:
                    return (get_node_loc(node.rightortop,point,node))
                    
                
        def find_point(node,min_=0):
            
            import math
            d = round(math.sqrt((p-points[0]).lensq()))
            qu_space1 = (Vec(p.x-d, p.y - d),Vec(p.x+d, p.y + d))
            j =  (self.points_in_range(qu_space1))
          #  print('poll these', j)
            minimum = float('Inf')
            sol = None
            for i in j:
                val = (math.sqrt((p-i).lensq()))
                if val < minimum:
                    minimum = val
                    sol = i
            return(sol)
        return find_point(get_node_loc(self, p))
    
    
    
    

    
    
    def plot(self, axes, top, right, bottom, left, depth=0):
        """Plot the the kd tree. axes is the matplotlib axes object on
           which to plot, top, right, bottom, left are the coordinates of
           the bounding box of the plot.
        """

        if self.is_leaf:
            axes.plot([p.x for p in self.points], [p.y for p in self.points], 'bo')
            if self.LABEL_POINTS:
                for p in self.points:
                    axes.annotate(p.label, (p.x, p.y),
                    xytext=(p.x + self.LABEL_OFFSET_X, p.y + self.LABEL_OFFSET_Y))
        else:
            if self.axis == 0:
                axes.plot([self.coord, self.coord], [bottom, top], '-', color='gray')
                self.leftorbottom.plot(axes, top, self.coord, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, bottom, self.coord, depth + 1)
            else:
                axes.plot([left, right], [self.coord, self.coord], '-', color='gray')
                self.leftorbottom.plot(axes, self.coord, right, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, self.coord, left, depth+1)
        if depth == 0:
            axes.set_xlim(left, right)
            axes.set_ylim(bottom, top)
       
    
    def __repr__(self, depth=0):
        """String representation of self"""
        if self.is_leaf:
            return depth * 2 * ' ' + "Leaf({})".format(self.points)
        else:
            s = depth * 2 * ' ' + "Node({}, {}, \n".format(self.axis, self.coord)
            s += self.leftorbottom.__repr__(depth + 1) + '\n'
            s += self.rightortop.__repr__(depth + 1) + '\n'
            s += depth * 2 * ' ' + ')'  # Close the node's opening parens
            return s