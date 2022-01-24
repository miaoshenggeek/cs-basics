# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from typing import List, Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def helper(root,remainSum,res,ans):
            if not root:return
            res.append(root.val)
            remainSum-=root.val
            if not root.left and not root.right and remainSum==0:
                ans.append(res[:])
            else:    #前面不return，就要加上else
                helper(root.left,remainSum,res,ans)
                helper(root.right,remainSum,res,ans)
            res.pop() 
            # We need to pop the node once we are done processing ALL of it's subtrees--backtracking
            
        ans=[]
        helper(root,targetSum,[],ans)
        return ans
    #Depth First Traversal | Recursion time O(N**2) Space  O(N)

#1022
#The number of nodes in the tree is in the range [1, 1000].Node.val is 0 or 1
def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def helper(root,path):
            nonlocal res
            path+=str(root.val)
            if root.left:helper(root.left,path)
            if root.right:helper(root.right,path)
            if not root.left and not root.right:
                #print(path)
                res+=int(path,2)
                return    
        res=0
        path=""
        helper(root,path)
        return res
#124. Binary Tree Maximum Path Sum  ##long path for tree with left+root+right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
            # naive: traverse once to make adjacency list, then find max subgraph
            # leveraging subtrees...
            # recurse down until leaf
            # go up, return max(root,left+root,right+root) BUT check left, right, root+left+right against global max
            
            def maxPathSumSubtree(root: Optional[TreeNode]) -> int:
                if not root.left and not root.right:
                    return root.val
                left_val = maxPathSumSubtree(root.left) if root.left else float('-inf')
                right_val = maxPathSumSubtree(root.right) if root.right else float('-inf')
                dfs_max = root.val+max(left_val, right_val,0) #carry
                nonlocal max_sum
                max_sum = max(max_sum, dfs_max,left_val, right_val, root.val + left_val + right_val) #rt
                #print(dfs_max,max_sum)
                return dfs_max ###method--recursion with return value
            
            max_sum = float('-inf')
            return max(maxPathSumSubtree(root), max_sum) #max_sum may not update if only one node