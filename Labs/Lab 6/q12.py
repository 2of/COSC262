class Node:
    """Represents an internal node in a Huffman tree. It has a frequency count
       and left and right subtrees, assumed to be the '0' and '1' children
       respectively.
    """
    def __init__(self, count, left, right):
        self.count = count
        self.left = left
        self.right = right

    def __str__(self, level=0):
        return ((2 * level) * ' ' + f"Node({self.count},\n" +
            self.left.__str__(level + 1) + ',\n' +
            self.right.__str__(level + 1) + ')')

    def is_leaf(self):
        return False

class Leaf:
    """A leaf node in a Huffman encoding tree. Contains a character and its
       frequency count.
    """
    def __init__(self, count, char):
        self.count = count
        self.char = char

    def __str__(self, level=0):
        return (level * 2) * ' ' + f"Leaf({self.count}, '{self.char}')"

    def is_leaf(self):
        return True
        
        
    
def huffman_decode(s, huffman_tree):
    
    code = []
    
    
    det(str[1:],tree.left,depth+1))
    
    def add_to(stri_,tree):
      result = ''
      total_depth = 0
      while(stri_):
        char, depth = (decode(stri_[total_depth:],tree,0))
        stri_ = stri_[depth:]
        result += char
      return result
    return add_to(s,tree)