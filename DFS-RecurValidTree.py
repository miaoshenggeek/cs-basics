from typing import List


def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
    if len(edges) != n - 1: return False
    
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)
    
    seen = set()
    
    def dfs(node, parent):
        if node in seen: return;
        seen.add(node)
        for neighbour in adj_list[node]:
            if neighbour == parent:
                continue
            if neighbour in seen:
                return False
            result = dfs(neighbour, node)
            if not result: return False
        return True
    
    # We return true iff no cycles were detected,
    # AND the entire graph has been reached.
    return dfs(0, -1) and len(seen) == n

def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
    if len(edges) != n - 1: return False
    
    # Create an adjacency list.
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)
    
    # We still need a seen set to prevent our code from infinite
    # looping if there *is* cycles (and on the trivial cycles!)
    seen = set()

    #end of recursion,doesn't care about cycle,iff connected and #edges=#node-1<=>valid tree
    def dfs(node):  #dfs on the start node instead of all nodes
        if node in seen: return  
        seen.add(node)
        for neighbour in adj_list[node]:
            dfs(neighbour)

    dfs(0)
    return len(seen) == n