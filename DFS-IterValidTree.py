from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:return False
        
        adj_list=[[] for _ in range(n)]
        for A,B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)
        #print(adj_list)
        parent={0:-1} #0 as root, each node in a valid tree can act as root
        stack=[0]
        while stack:
            node=stack.pop()
            for neighbor in adj_list[node]:
                if neighbor==parent[node]:# each edge is double directed in adj_list
                    continue
                if neighbor in parent: #cycle
                    return False
                parent[neighbor]=node #
                stack.append(neighbor)
                #print(stack,parent)
        return len(parent)==n

def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
    if len(edges) != n - 1: return False
    
    # Create an adjacency list.
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)
    
    # We still need a seen set to prevent our code from infinite
    # looping if there *is* cycles (and on the trivial cycles!)
    seen = {0}
    stack = [0]
    
    while stack:
        node = stack.pop()
        for neighbour in adj_list[node]:
            if neighbour in seen:
                continue
            seen.add(neighbour)
            stack.append(neighbour)
    
    return len(seen) == n