# Definition for a binary tree node.
import bisect
from typing import List, Optional
from bisect import bisect_left


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(preorder,inorder):
            if not preorder or not inorder:
                return
            a=preorder[-1]
            root=TreeNode(a)    
            preorder.pop()
            b=inorder.index(a) #O(n)
            ## build a hashmap to store value -> its index relations
            
            root.left=helper(preorder,inorder[:b])
            root.right=helper(preorder,inorder[b+1:])
            return root
        #inorder_index_map = {}
        #for index, value in enumerate(inorder):
        #   inorder_index_map[value] = index
        preorder.reverse()
        return helper(preorder,inorder)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def array_to_tree(left, right): #to pass index instead of arr,use left and right
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right: return None
            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            preorder_index += 1
            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)
            return root
        preorder_index = 0
        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index
        return array_to_tree(0, len(preorder) - 1)

class Solution:
    #O(n)
    def bstFromPreorder(self, A: List[int]) -> Optional[TreeNode]:
        return self.buildTree(A, float('inf'))
    def buildTree(self, A, bound):
        if not A or A[0] > bound: return None
        node = TreeNode(A.pop(0))
        node.left = self.buildTree(A, node.val)
        node.right = self.buildTree(A, bound)
        return node

    #O(n log n)
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:return None
        a=preorder[0]
        root=TreeNode(a)
        preorder.pop(0)
        idx=0
        if preorder:
            idx=bisect_left(preorder,a)
            root.left=self.bstFromPreorder(preorder[:idx])
            root.right=self.bstFromPreorder(preorder[idx:])
        return root
    
    def bstFromPreorder(self, A):
        if not A: return None
        root = TreeNode(A[0])
        i = bisect.bisect(A, A[0])
        root.left = self.bstFromPreorder(A[1:i])
        root.right = self.bstFromPreorder(A[i:])
        return root
    #O(n log n)
    def bstFromPreorder(self, A):
        def helper(i, j):
            if i == j: return None
            root = TreeNode(A[i])
            mid = bisect.bisect(A, A[i], i + 1, j)
            root.left = helper(i + 1, mid)
            root.right = helper(mid, j)
            return root
        return helper(0, len(A))

#889. Construct Binary Tree from Preorder and Postorder Traversal
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:return
        root=TreeNode(preorder[0])
        preorder.pop(0)
        postorder.pop()
        if preorder and postorder:
            v=postorder[-1]
            t=preorder[0]
            idx=preorder.index(v)
            idt=postorder.index(t)
            if idx==0: root.left=self.constructFromPrePost(preorder,postorder)
            # same with idx==0
            # elif idt==len(postorder)-1:
            #    root.right=self.constructFromPrePost(preorder,postorder)
            else:
                root.left=self.constructFromPrePost(preorder[:idx],postorder[:idt+1])
                root.right=self.constructFromPrePost(preorder[idx:],postorder[idt+1:])
        return root


    preIndex, posIndex = 0, 0
    def constructFromPrePost(self, pre, post):
        root = TreeNode(pre[self.preIndex])
        self.preIndex += 1
        if (root.val != post[self.posIndex]):
            root.left = self.constructFromPrePost(pre, post)
        if (root.val != post[self.posIndex]):
            root.right = self.constructFromPrePost(pre, post)
        self.posIndex += 1
        return root
    def constructFromPrePost(self, pre, post):
        stack = [TreeNode(pre[0])]
        j = 0
        for v in pre[1:]:
            node = TreeNode(v)
            while stack[-1].val == post[j]:
                stack.pop()
                j += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]

    #701. Insert into a Binary Search Tree
    #TC,TS O(H),recursion stack
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            new=new=TreeNode(val)
            root=new
        if val>root.val:
            root.right=self.insertIntoBST(root.right,val)
        if val<root.val:
            root.left=self.insertIntoBST(root.left,val)
        return root
    #TC O(H)    TS O(1) 
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            # insert into the right subtree
            if val > node.val:
                # insert right now
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            # insert into the left subtree
            else:
                # insert right now
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
        return TreeNode(val)