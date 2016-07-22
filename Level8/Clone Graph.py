# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        from collections import deque
        q = deque()
        h = {}
        q.append(node)
        cnode = UndirectedGraphNode(node.label)
        h[node] = cnode
        while(len(q) > 0):
            t = q[0]
            q.popleft()
            for i in t.neighbors:
                if i not in h:
                    copy = UndirectedGraphNode(i.label)
                    h[i] = copy
                    q.append(i)
                h[t].neighbors.append(h[i])

        return cnode