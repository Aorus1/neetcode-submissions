"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(new_node, node) -> Optional['Node']:
            if (node in visited):
                return
            print(node.val)

            visited.add(node)
            hm[node.val] = new_node
            new_node.val = node.val
            if node.neighbors is None:
                new_node.neighbors = None
                return
            for neighbor in node.neighbors:
                if neighbor in visited:
                    new_node.neighbors.append(hm[neighbor.val])
                    continue
                new_neighbor = Node(neighbor.val, [])
                new_node.neighbors.append(new_neighbor)
                dfs(new_neighbor, neighbor)


            
                

            

        if node is None:
            return None
        visited = set()
        hm = {}
        root = Node()
        dfs(root, node)





        return root
        


        