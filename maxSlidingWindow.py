#239
from typing import Deque, List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #maintain a deque to record the cur window
        #but the size of deque != k , discard num that will not be used for compare
        #Ensure the deque window only has decreasing elements. 
        #Make suer the leftmost element is always the largest.   ##### key for O(n)
        q=Deque()
        res=[]
        for i,v in enumerate(nums):
            
            while q and nums[q[-1]]<=v:
                q.pop()    #discard num smaller than cur
                
            q.append(i)  #put cur to q
            
            if q[0]<=i-k:q.popleft()  ## cut num outside window from idx<=i-k
                
            if i>=k-1:res.append(nums[q[0]]) ## starting max window from idx= k-1
            
        return res