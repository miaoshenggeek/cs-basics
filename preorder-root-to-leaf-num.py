from typing import Optional

from f_Subtree_Another_Tree import TreeNode

#129
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Iterative solution
        # Push root into stack.
        # While stack is not empty:
        # Pop out a node from stack and update the current number.
        # If the node is a leaf, update root-to-leaf sum.
        # Push right and left child nodes into stack.
        # Return root-to-leaf sum.
        """
        def preorder(r, curr_number):
            nonlocal root_to_leaf
            if r:
                curr_number = curr_number * 10 + r.val
                # if it's a leaf, update root-to-leaf sum
                if not (r.left or r.right):
                    root_to_leaf += curr_number
                    
                preorder(r.left, curr_number)
                preorder(r.right, curr_number) 
        
        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf
        """
        def preorder(root,num=0):
            nonlocal res
            if root:
                num=num*10+root.val
                if not root.left and not root.right:
                    res+=num    
                preorder(root.left,num)
                preorder(root.right,num)
        res=0
        preorder(root,0)
        return res

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root,path):
            nonlocal res
            if not root:
                return
            path=path*10+root.val #1     
            dfs(root.left,path)     #2
            dfs(root.right,path)    #3
            #
            if not root.right and not root.left: #4
                res+=path 
        path=0
        res=0
        dfs(root,path)
        return res
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def preorder(root,num=0):
            if not root:
                #print(num)
                return num
            num=num*10+root.val
            if not root.left: return preorder(root.right,num)
            elif not root.right: return preorder(root.left,num)
            else: return preorder(root.right,num)+preorder(root.left,num)
        res=preorder(root,0)
        return res
    """
    [1,2,3]
    [4,9,0,5,1]
    [4,9,0,null,1]"""