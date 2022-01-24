from typing import List, Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(n: TreeNode, val: int, path: List[str]) -> bool:
            if n.val == val:
                return True
            if n.left and find(n.left, val, path):
                path += "L"
            elif n.right and find(n.right, val, path):
                path += "R"
            return path
            #not really backtrack
        s, d = [], []
        find(root, startValue, s)
        find(root, destValue, d)
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        return "".join("U" * len(s)) + "".join(reversed(d))
def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(root,v):
            if not root:return 
            if root.val==v:
                path.append("".join(res))
                #print(path)
                return
            res.append("L")
            find(root.left,v)
            res.pop()
            res.append("R")
            find(root.right,v)
            res.pop()
        res=[]  
        path=[]
        find(root,startValue)
        find(root,destValue)
        pathS=path[0]
        pathD=path[1]
        #print(pathS,pathD)
        prefix=0
        for i in range(len(pathS)):
            if i<len(pathD) and pathS[i]==pathD[i]:
                #print("same")
                prefix+=1
                continue
            prefix=i
            break
        #print(prefix)
        pathS=pathS[prefix:]
        pathD=pathD[prefix:]
        
        return "U"*len(pathS)+pathD