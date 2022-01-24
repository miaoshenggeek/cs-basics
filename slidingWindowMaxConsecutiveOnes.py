from typing import List

#1004  
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        start=0
        end=1
        cur=1-nums[start]
        res=k
        n=len(nums)
        while end<n:
            while (cur==k and nums[end]==0) or cur>k:
                cur=cur-(1-nums[start])
                start+=1   
            if nums[end]==0 and cur<k:
                cur+=1   
            end+=1
            res=max(res,end-start)
            #print(cur,res,end,start)
        return res'''
        left = right = 0

        for right in range(len(nums)):
            #right moves at least k steps faster than left,
            #right can move (sum of front 1) + k steps befor decrement k to 0, 
            k -= 1-nums[right]  #if nums[right] == 0:
            # else no impact to K
            # A negative k denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if k < 0:
                #If the left element to be thrown out is zero we increase k.
                k += 1-nums[left]#if nums[left] == 0:
                #Since we have to find the MAX window, we never reduce the size of the window. 
                left += 1

        return right - left + 1
#487. Max Consecutive Ones II, only can flip one 0 to 1        
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zero=0
        start=0
        for i,v in enumerate(nums):
            if v==0:
                zero+=1
            if zero>1: 
                zero-=1-nums[start]
                start+=1
        return i-start+1

#k is the window, if there is no k, there is no window
def findMaxConsecutiveOnes(self, nums):
  return max(map(len, ''.join(map(str, nums)).split('0')))