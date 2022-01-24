from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, num: int, pre: List[List[int]]) -> bool:
        #check if there is a circle in pre
        #enumerate each course (vertex), to check if it could form cyclic dependencies
        #  (i.e. a cyclic path) 
        # starting from this course-->enumerate each vertex to check if it go back to start
        dic=defaultdict(list)
        for i,j in pre:
            dic[i].append(j)
        #print(dic)
        def dfs(i):# postorder DFS
            if checked[i]:return True #base case to prevent endless recurse
            if path[i]:return False 
            path[i]=True # mark the nodes we visited
            ret=True 
            for nei in dic[i]:
                ret=dfs(nei)
                if not ret:break
            #after the visits of children, we come back to process the node itself
            # remove the node from the path
            path[i]=False  #remove the breadcrumbs for each iteration
            # Now that we've visited the nodes in the downstream,
            # we complete the check of this node.
            checked[i]=True
            return ret
        path=[False for i in range(num)]
        checked=[False for i in range(num)]  #whether we have done the cyclic check starting from a particular node.
        for node in range(num):
            if not dfs(node):return False
        return True