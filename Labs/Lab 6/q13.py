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
        
        
def huffman_encode(s, huffman_tree):
  pass
  table = {}

  def make_encodes(tree, so_far = ''):
    if tree.is_leaf():
      add_to_table(so_far,tree.char)
      return (so_far, tree.char)
    else:
      return (make_encodes(tree.left,so_far + '0'),make_encodes(tree.right,so_far + '1'))
  
  
  def add_to_table(encoding, char): 
    table[char] = encoding
    #print(table)
    
    
  def encode(s,table,res = ''):
    if len(s) == 0:
      return res
    else: 
      return (encode(s[1:],table,res + table.get(s[0])))
  make_encodes(huffman_tree)
  return encode(s, table)
