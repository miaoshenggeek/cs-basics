import collections
from typing import Deque, List

#862 Shortest Subarray with Sum at Least K
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        d = collections.deque([[0, 0]])
        res, cur = float('inf'), 0
        for i, a in enumerate(A):
            cur += a   # prefix sum
            while d and cur - d[0][1] >= K:
                res = min(res, i + 1 - d.popleft()[0])
            while d and cur <= d[-1][1]:
                d.pop()
            d.append([i + 1, cur])
        return res if res < float('inf') else -1
    """
    Why keep the deque increase?
    If B[i] <= B[d.back()] and moreover we already know that i > d.back(),
    it means that compared with d.back(),
    B[i] can help us make the subarray length shorter and sum bigger. 
    So no need to keep d.back() in our deque."""

#209 only positive integers
class Solution: #sliding window (two pointer)  O(n) 
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        d=Deque([[-1,0]])
        cur=0
        res=float("inf")
        for i,v in enumerate(nums):
            cur+=v
            while d and cur-d[0][1]>=target:
                res=min(res,i-d.popleft()[0])
            d.append([i,cur])
        return res if res<float("inf") else 0
        """
        l=r=0
        add=0
        res=10**5+1
        while r<len(nums):
            add+=nums[r]
            while add>=target:
                res=min(res,r-l+1)
                add-=nums[l]
                l+=1
            r+=1
        return res if not res==10**5+1 else 0
        """
        
class Solution: #binary search can be used on prefix sum to find the largest left idx O(n log n)
    def minSubArrayLen(self, target, nums):
        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n
        left = 0
        for right, n in enumerate(nums):
            if n >= target:
                left = self.find_left(left, right, nums, target, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    def find_left(self, left, right, nums, target, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left