# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Collection, Optional
from f_Subtree_Another_Tree import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], t: int) -> int:
        count=Collection.Counter()
        count[0]=1
        cursum=0
        pre=root
        self.res=0
        self.preorder(pre,cursum,t,count)
        return self.res
        
        
    def preorder(self,root,cursum,t,count):
        if not root:return
        cursum+=root.val
        self.res+=count[cursum-t]
        count[cursum]+=1
        self.preorder(root.left,cursum,t,count)
        self.preorder(root.right,cursum,t,count)
        # remove the current sum from the hashmap
        # in order not to use it during 
        # the parallel subtree processing
        count[cursum] -= 1