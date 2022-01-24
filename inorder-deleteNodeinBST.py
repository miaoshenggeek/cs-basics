#Inorder traversal of BST is an array sorted in the ascending order.
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

#Successor = "after node", i.e. the next node, or the smallest node after the current one.
#It's also the next node in the inorder traversal. 
# To find a successor, go to the right once and then as many times to the left as you could.
#if node has no right child, successor is the parent, need to go back, so use predecessor instead.
def successor(root):
    root = root.right
    while root.left:
        root = root.left
    return root
#Predecessor = "before node", i.e. the previous node, or the largest node before the current one.
#It's also the previous node in the inorder traversal. 
# To find a predecessor, go to the left once and then as many times to the right as you could.
def predecessor(root):
    root = root.left
    while root.right:
        root = root.right
    return root

class Solution:
    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val
        
    def deleteNode(self, root, key: int) :
        if not root:
            return None
        
        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child    
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root