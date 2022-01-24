"""
L = Empty list that will contain the sorted elements
S = Set of all nodes with no incoming edge  (set of leaves)

while S is non-empty do
    remove a node n from S
    add n to tail of L
    for each node m with an edge e from n to m do (neighbor if a leaf)
        remove edge e from the graph
        if m has no other incoming edges then    (new leaf after pruning)
            insert m into S

if graph has edges then
    return error   (graph has at least one cycle)
else 
    return L   (a topologically sorted order)
"""
from typing import List


class Solution:
    def findOrder(self, num: int, pre: List[List[int]]) -> List[int]:
        l=[]
        graph=[set() for _ in range(num)]
        g2=[set() for _ in range(num)]
        s=[]
        for i,j in pre:
            graph[i].add(j)
            g2[j].add(i)
        #print(graph)
        for i,leaf in enumerate(graph):
            if not leaf:
                s.append(i)
        while s:
            #print(s)
            node=s.pop()
            l.append(node)
            neighs=g2[node]
            for newnode in neighs:
                #print(newnode,leaves,s,l)
                graph[newnode].remove(node)
                if not graph[newnode]:
                    if newnode not in l and newnode not in s:
                        s.append(newnode)
                
        for i in graph:
            if i!=set():return []
        else:return l