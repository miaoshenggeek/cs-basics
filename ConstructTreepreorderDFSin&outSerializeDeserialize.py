# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        rt=[]
        def helper(root):
            if not root:
                rt.append("#,")
                return
            rt.append(str(root.val)+",")
            helper(root.left)
            helper(root.right)
        helper(root)
        return "".join(rt)


            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        '''
        arr=data.split(",")
        def helper(arr):
            if arr[0]=="#":
                arr.pop(0)
                return None
            root=TreeNode(arr[0])
            arr.pop(0)
            root.left=helper(arr)
            root.right=helper(arr)
            return root
        return helper(arr)'''
    def deserialize(self, data):
        arr=data.split(",")
        def helper(arr):
            if arr[-1]=="#":
                arr.pop()
                return None
            root=TreeNode(arr[-1])
            arr.pop()
            root.left=helper(arr)
            root.right=helper(arr)
            return root
        arr.reverse()
        return helper(arr)

        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split(","))    #how to use iterator
        return doit()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

class Codec:
    def serialize(self, root):
        # take care of base cases
        # if a node is empty, add 'x' to string
        # you can set 'x' to any mark as you want
        if not root: return 'x'
        # preoder(Root->left->right)
        # ex,
        #     1
        #    / \
        #   2   3
        #      / \
        #     4   5 
        # 
        # return (1, (2, 'x', 'x'), (3, (4, 'x', 'x'), (5, 'x', 'x')))
        # if you look at the return statement very closely, it is actually very intuitive
        # for value 1, you have 2 as left child and 3 as right child
        # for value 2, you have 'x'(None) as left child and 'x'(None) as right child which indicates it is a leaf node
        return root.val, self.serialize(root.left), self.serialize(root.right)

    def deserialize(self, data):
        #######################INTUITION#########################
        # The initial data string will be something like below:
        # (1, (2, 'x', 'x'), (3, (4, 'x', 'x'), (5, 'x', 'x')))
        # if you loop through string: 
        # 1                                 -> this is node value
        # (2, 'x', 'x')                     -> this is node left
        # (3, (4, 'x', 'x'), (5, 'x', 'x')) -> this is node right
        ########################################################
        # always take care of base case: if the node's value is 'x' then return None
        if data[0] == 'x': return None
        # create new treenode for node value
        node = TreeNode(data[0])
        # do the recursive to unpack string value
        node.left = self.deserialize(data[1])
        node.right = self.deserialize(data[2])
        # return the new TreeNode that we just created
        return node