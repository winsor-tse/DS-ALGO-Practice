class TreeNode:
    def __init__(self, value) -> None:
        self.v = value
        self.left = None
        self.right = None
def pre_order(t):
    if t:
        print(t.v)
        #add visited if its connected graph
        pre_order(t.left)
        pre_order(t.right)
    
if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(4)
    p.right.right = TreeNode(5)
    p.left.right = TreeNode(6)
    """
            1
        2       4
           6        5
    """
    pre_order(p)


