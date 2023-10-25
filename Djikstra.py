class graph:
    def __init__(self, edges, n_nodes) -> None:
        #structure of edges
        #[u,v,w] u - > srouce node, v -> target node, w -> weight
        self.edges = edges
        self.n_nodes = n_nodes
    def adj(self):
        #create an adjency dictionary
        import collections
        a = collections.defaultdict(list)
        for u,v,w in self.edges:
            a[u].append([v,w])
        return a

def djikstra(adj, start_node):
    import heapq
    #create pq with value of 0 and start node
    #assume that start node may or may not exist
    #value and startnode or vertix
    p_q = [(0,start_node)]
    #weight and vertix
    shortest_path = {}
    while p_q:
        w, v = heapq.heappop(p_q)
        if v not in shortest_path:
            shortest_path[v] = w
            #start the dfs here
            for v_i, w_i in adj[v]:
                #add the weights and vertix
                heapq.heappush(p_q, (w + w_i, v_i))
                print(p_q)
    return shortest_path
if __name__ == '__main__':
    print('hello')
    g = graph(edges = [[2,1,1],[2,3,1],[3,4,1]], n_nodes=4)
    adj = g.adj()
    print(adj)
    #prints shortest path starting from start_node to all other nodes
    print(djikstra(adj, 2))