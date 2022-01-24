# Definition for a binary tree node.
import collections
from typing import DefaultDict

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root in (p,q):
            return root        
        left, right = self.lowestCommonAncestor(root.left,p,q), self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        return left or right
        
    #special situation for BST instead of BT
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:return
        if p.val>q.val:p,q=q,p
        if p.val<=root.val and q.val>=root.val:return root
        if root==p or root==q:return root
        return self.lowestCommonAncestor(root.left,p,q) or self.lowestCommonAncestor(root.right,p,q) 

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic=DefaultDict(int)
        dic[root]=None
        def findpi(root):
            if not root:return
            #dic[root.val].append(root.val)
            if root.left:dic[root.left]=root
            if root.right:dic[root.right]=root
            findpi(root.left)
            findpi(root.right)
        findpi(root)
        """
        #debug, print clean node.val
        for i,j in dic.items():
            if j==None:temp="None"
            else:temp=j.val
            print(i.val,temp,end=",",sep=":")
        print()"""
        #if len(dic[p])>len(dic[q]):p,q=q,p
        
        a=[p]
        
        while dic[p]:
            a.append(dic[p])
            p=dic[p]
        """
        #debug, print clean node.val
        for i in a:
            if i==None:temp="None"
            else:temp=i.val
            print(temp,end=",")"""
        while q not in a:
            q=dic[q]
        
        return q
    
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """
        I took a different approach. Do BFS and keep track of all the nodes of the last level. 
        At each level, keep a hashMap to track the parent node.
        If there is only one node at the last level, then you return that. 
        Otherwise, for each node at the last level rollback with the parent. 
        Add the parents to a set and do that recursively until you have one node.
        Runtime: O(n)
        Space: O(n)"""   
        # The result of a subtree is:
        # Result.node: the largest depth node that is equal to or
        #              an ancestor of all the deepest nodes of this subtree.
        # Result.dist: the number of nodes in the path from the root
        #              of this subtree, to the deepest node in this subtree.
        Result = collections.namedtuple("Result", ("node", "dist"))
        def dfs(node):
            # Return the result of the subtree at this node.
            if not node: return Result(None, 0)
            L, R = dfs(node.left), dfs(node.right)
            if L.dist > R.dist: return Result(L.node, L.dist + 1)
            if L.dist < R.dist: return Result(R.node, R.dist + 1)
            return Result(node, L.dist + 1)
        def helper(root):
            if not root: return 0, None
            h1, lca1 = helper(root.left)
            h2, lca2 = helper(root.right)
            if h1 > h2: return h1 + 1, lca1
            if h1 < h2: return h2 + 1, lca2
            return h1 + 1, root
        return helper(root)[1]

        return dfs(root).node
        '''self.lca, self.deepest = None, 0
        def helper(node, depth):
            self.deepest = max(self.deepest, depth)
            if not node:
                return depth
            left = helper(node.left, depth + 1)
            right = helper(node.right, depth + 1)
            if left == right == self.deepest:
                self.lca = node
            return max(left, right)
        helper(root, 0)
        return self.lca'''