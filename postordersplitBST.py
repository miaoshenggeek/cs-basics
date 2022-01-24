# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        #在每次遍历到叶子节点之后，对root的左右节点进行储存并且将其传送到上一层，是post-order的思想。
        if not root:
            return None,None
        elif root.val<target:#==可以合并到这里<=结果一样，但分开写比较好理解
            bns=self.splitBST(root.right,target)
            root.right=bns[0]
            return root,bns[1]
        elif root.val==target:
            right=root.right
            root.right=None
            return root,right
        else:
            bns=self.splitBST(root.left,target)
            root.left=bns[1]
            return bns[0],root