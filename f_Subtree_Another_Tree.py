# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        string_s = self.traverse_tree(s)
        string_t = self.traverse_tree(t)
        if string_t in string_s:
            return True
        return False
    def traverse_tree(self, s):
        if s:
            print (f"#{s.val} {self.traverse_tree(s.left)} {self.traverse_tree(s.right)}")
            #print('#{}{}{}'.format(n.val, f(n.left), f(n.right)))
            return f"#{s.val} {self.traverse_tree(s.left)} {self.traverse_tree(s.right)}"
        return None
    '''def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: 
        def f(n): #O(S)+O(T)
            if not n:
                return 'None'
            #print('#{}{}{}'.format(n.val, f(n.left), f(n.right)))
            return '#{}{}{}'.format(n.val, f(n.left), f(n.right))
        
        return f(subRoot) in f(root) '''
        #O(m * n) where m and n are lengths of s1 and s2 respectively. 
        #A nested loop is used the outer loop runs from 0 to N-M and inner loop from 0 to M so the complexity is O(m*n).
    
    #def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: # O(|s| * |t|)
    """
        def match(root,sb):
            if not sb or not root:return sb==root # sb is root
            #if not sb and not root:return True
            #elif not sb or not root:return False
            return root.val==sb.val and match(root.left,sb.left) and match(root.right,sb.right)           
        if match(root,subRoot):return True
        if not root:return False
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)"""

    
        
        
        
        
'''
[3,4,5,1,None,2]
[3,1,2]
[1,1]
[1]
[3,4,5,1,2]
[4,1,2]
[3,4,5,1,2,None,None,None,None,0]
[4,1,2]
'''