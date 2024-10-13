def greatest_node(root: 'Node') -> int:
    if root is None:
        return float('-inf')
    return max(root.value, greatest_node(root.left_child), greatest_node(root.right_child))

class Node:
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child