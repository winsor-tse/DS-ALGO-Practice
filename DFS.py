class TreeNode:
    def __init__(self, value) -> None:
        self.v = value
        self.left = None
        self.right = None
def pre_order(t, l):
    if t:
        #print or add to a list
        l.append(t.v)
        #add visited if its connected graph
        pre_order(t.left, l)
        pre_order(t.right, l)

def pre_order_iterative(t, l):
    stk = []
    stk.append(t)
    while stk:
        curr = stk.pop()
        # can be replaced with a print as needed
        l.append(curr.v)
        #note that you append right first because you pop out the end
        if curr.right:
            stk.append(curr.right)
        if curr.left:
            stk.append(curr.left)

def inorder(t):
    if t:
        inorder(t.left)
        print(t.v)
        inorder(t.right)
#TODO: inorder iterative

def postorder(t):
    if t:
        postorder(t.left)
        postorder(t.right)
        print(t.v)
#TODO: post order iterative

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
    r = []
    pre_order(p,r)
    print(r)
    r= []
    pre_order_iterative(p,r)
    print(r)
    inorder(p)
    postorder(p)


