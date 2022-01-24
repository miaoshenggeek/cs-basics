from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=2: return [i for i in range(n)]
        graph=[set() for i in range(n)]#{i:set() for i in range(n)}
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        q=[]
        for key,value in enumerate(graph):#graph.items()
            if len(value)==1: q.append(key)
        remaining_nodes=n
        
        while remaining_nodes>2:
            remaining_nodes-=len(q)
            new_q=[]
            while q:
                leaf=q.pop()
                neighbor=graph[leaf].pop()#
                graph[neighbor].remove(leaf)
                if len(graph[neighbor])==1:
                    new_q.append(neighbor)
            q=new_q
        return q
#4,[[1,0],[1,2],[1,3]]
# 6,[[3,0],[3,1],[3,2],[3,4],[5,4]]