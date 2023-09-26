class TreeNode:
    def __init__(self, value) -> None:
        self.v = value
        self.left = None
        self.right = None

#BFS for TreeNodes
def BFS(t):
    #regular BFS
    r = []
    import collections
    q = collections.deque()
    q.append(t)
    while q:
        #popLeft is the same as pop(0)
        #FIFO
        curr = q.popleft()
        #can also append to list and return
        r.append(curr.v)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    return r

#BFS level Order for Tree Nodes
def BFS_Level_Order(t):
    r = []
    import collections
    q = collections.deque()
    q.append(t)
    while q:
        #temp list
        new_l = []
        for i in range(len(q)):
            curr = q.popleft()
            #can also append to list and return
            new_l.append(curr.v)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        r.append(new_l)
    return r

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
    print(BFS(p))
    print(BFS_Level_Order(p))