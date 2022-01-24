from typing import List, Optional
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def helper(node):
            if not node:return
            nonlocal last, first
            helper(node.left)
            if last:
                last.right=node
                node.left=last
            else:
                first=node
            last=node
            helper(node.right)
            
        if not root:return
        first,last=None,None
        helper(root)
        last.right=first
        first.left=last
        return first
def treeToDoublyList(self, root: 'Node') -> 'Node':
    
    if not root:
        return None
    
    stack = []
    first, curr, last = None, root, None
    
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
            continue
        if stack:
            curr = stack.pop()
            if not first:
                first = curr
            if last:
                last.right = curr
                curr.left = last
            last = curr
            curr = curr.right
    
    first.left = last
    last.right = first
    
    return first

def inorderTraversal(self, root: Optional[Node]) -> List[int]:
    res=[]
    def helper(root):
        if not root: return
        helper(root.left)
        res.append(root.val)
        helper(root.right)
        return res
        
    return helper(root)

def inorderTraversal(self, root):
    ans = []
    stack = []

    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            tmpNode = stack.pop()
            ans.append(tmpNode.val)
            root = tmpNode.right

    return ans