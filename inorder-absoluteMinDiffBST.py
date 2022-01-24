class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        mini = float("inf")
        stack = []
        cur = root
        pre = None 
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre:
                    mini = min(mini, cur.val - pre.val)
                pre = cur
                cur = cur.right
        return mini 
        #[4,2,6,1,3]