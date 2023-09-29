#create BSST here and loop through it
class BST:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def validate_BST(bst) -> bool:
    """
    A valid BST is defined as follows:
    The left 
    subtree
    of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
    """
    return False

if __name__ == '__main__':
    bst = BST(1)
    bst.left = BST(2)
    bst.right = BST(3)
