from typing import List
import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        self.totalSum=sum(w)
        s=0
        self.preSum=[]
        for i in w:
            s+=i
            self.preSum.append(s)
   
        

    def pickIndex(self) -> int:
        #target=random.random()*self.totalSum
        #target=random.randint(1,self.totalSum)
        #a=bisect.bisect_left(self.preSum,target)
        
        #target=random.randrange(self.totalSum)
        target=random.randint(0,self.totalSum-1)
        a=bisect.bisect_right(self.preSum,target)
        return a
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()