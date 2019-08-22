class Node:
    """Represents an internal node in a Huffman tree. It has a frequency count
       and left and right subtrees, assumed to be the '0' and '1' children
       respectively.
    """
    def __init__(self, count, left, right,low_char):
        self.count = count
        self.left = left
        self.right = right
        self.low_char = low_char
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
    def __init__(self, count, char, low_char):
        self.count = count
        self.low_char = char
        self.char = char

    def __str__(self, level=0):
        return (level * 2) * ' ' + f"Leaf({self.count}, '{self.char}')"

    def is_leaf(self):
        return True
    


def get_mins(freq_table):
    freq_table = sorted(freq_table, key = lambda x: x.count)
    dupe_length = 0
    for i in freq_table[1:]:
        if i.count == freq_table[0].count:
            dupe_length += 1
        else:
            break
    if dupe_length:
        freq_table[0:dupe_length+1] = sorted(freq_table[0:dupe_length+1], key = lambda x: x.low_char)
        left = freq_table.pop(0)
        right = freq_table.pop(0)
    else:
        left = freq_table.pop(0)
        right = freq_table.pop(0)
    smallest_char = min(left.low_char, right.low_char)
    new_node = Node(left.count + right.count, left, right,smallest_char)
    freq_table.append(new_node)
    return freq_table
    

    
    


def make_leaves(frequencies):
    results = sorted([Leaf(count,char,char) for char,count in zip(frequencies,frequencies.values())], key = lambda x: x.count)
    return results



def huffman_tree(frequencies):
    freq_table = make_leaves(frequencies)
    while len(freq_table) != 1:
        freq_table =  (get_mins(freq_table))
    return freq_table[0]
    
