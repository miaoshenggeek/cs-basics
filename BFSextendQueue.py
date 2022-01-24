from typing import Deque, List

#339 Nested List Weight(height) Sum
class Solution:#NestedInteger
    def depthSum(self, nestedList: List) -> int:
        '''if not nestedList:return 0
        stack=[(1,nestedList)]
        res=0
        while stack:
            if stack[0][1]==[]:
                stack.pop(0)
                continue
            cur=stack[0][1].pop(0)
            if cur.isInteger():
                res+=stack[0][0]*cur.getInteger()
                #print(res)
            else:
                stack.append((stack[0][0]+1,cur.getList()))    
                #print(stack)
        return res'''
        
        queue = Deque(nestedList)
        depth = 1
        total = 0
        while len(queue) > 0:
            #print(len(queue))
            for i in range(len(queue)):
                nested = queue.pop()
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    queue.extendleft(nested.getList())
            depth += 1

        return total
    #429 n-ary tree level order
    def levelOrder(self, root) -> List[List[int]]:
        if not root:return 
        res=[[root.val]]
        que=root.children
        while que:
            ans=[]
            v=[]
            for i in que:
                ans.extend(i.children)
                v.append(i.val)
            que=[]
            if ans:que=ans
            if v:res.append(v)
        return res