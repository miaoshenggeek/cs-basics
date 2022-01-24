# Definition for a binary tree node.
# vertical traverse
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
from collections import defaultdict
import collections
from typing import Deque, List, Optional
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def DFS(node, row, column):
            if node:
                nonlocal min_column, max_column
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        DFS(root, 0, 0)

        # order by column and sort by row
        ret = []
        for col in range(min_column, max_column + 1):
            columnTable[col].sort(key=lambda x:x[0])
            colVals = [val for row, val in columnTable[col]]
            ret.append(colVals)

        return ret
        
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return
        dic=defaultdict(list)
        def helper(node,col,hei):
            dic[col].append([hei,node.val])   
            if node.left:
                helper(node.left,col-1,hei+1)
            if node.right:
                helper(node.right,col+1,hei+1)
        helper(root,0,0)
        res=[]
        #print(dic)
        for i in sorted(dic):
            cur=sorted(dic[i],key=lambda i: i[0])
            res.append([i[1] for i in cur])
        return res

    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0
        queue = Deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node:
                columnTable[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in range(min_column, max_column + 1)]

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return
        res=[]
        que=collections.deque([root])
        while que:
            size=len(que)
            cur=[]
            for i in range(size):
                node=que.popleft()
                cur.append(node.val)
                if node.left:que.append(node.left)
                if node.right:que.append(node.right)
            res.append(cur)
        return res