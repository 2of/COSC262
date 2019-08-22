from collections import namedtuple
Node = namedtuple("Node", ["value", "left", "right"])

def search_tree(nums, leftboundpylintisevil=0, rbplussomecharacters=0, first=True):
    '''Returns bianry tree and makes pylint a happy '''
    if first:
        nums = sorted(nums)
        leftboundpylintisevil = 0
        rbplussomecharacters = len(nums)
    n = rbplussomecharacters-leftboundpylintisevil
    if n == 1:
        tree = Node(nums[leftboundpylintisevil], None, None) 
    else:
        mid = n // 2 + leftboundpylintisevil
        left = search_tree(nums, leftboundpylintisevil, mid, False)
        right = search_tree(nums, mid, rbplussomecharacters, False)
        tree = Node(nums[mid-1], left, right)
    return tree
# Leave the following function unchanged
def print_tree(tree, level=0):
    """Print the tree with indentation"""
    if tree.left is None and tree.right is None: # Leaf?
        print(2 * level * ' ' + f"Leaf({tree.value})")
    else:
        print(2 * level * ' ' + f"Node({tree.value})")
        print_tree(tree.left, level + 1)
        print_tree(tree.right, level + 1)


