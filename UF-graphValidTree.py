from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #connected and no cycle
        uf=UF(n)
        for i,j in edges:#new edge already connected is cycle
            if uf.connected(i,j):return False
            uf.union(i,j)
        for i in range(1,n):#any node not connected to any node is disconnectivity
            if not uf.connected(0,i):return False   #return len(edges)==n-1
        return True
#Time O(n*C)  C<4 with path compression
#Space O(n) as the array size                
class UF:
    def __init__(self,n:int):
        self.pi=[i for i in range(n)]
        self.rank = [0 for i in range(n)]
    def find(self,x):
        if not self.pi[x]==x:
            return self.find(self.pi[x])#need to return here
        return self.pi[x]
    def connected(self,x,y):
        if self.find(x)==self.find(y):
            return True
        else:return False
    def union(self,x,y):
        u=self.find(x)
        v=self.find(y)
        if self.rank[u]>self.rank[v]:
            self.pi[v]=u
        elif self.rank[u]<self.rank[v]:
            self.pi[u]=v
        else:           
            self.pi[u]=v
            self.rank[v]+=1