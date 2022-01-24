from bisect import bisect_right
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # O(n^2 log n)
        nums.sort()
        diff = float('inf')
        for i, v1 in enumerate(nums):
            for j,v2 in enumerate(nums[i+1:]):
                v3=target-v1-v2
                hi=bisect_right(nums,v3,i+j+2)  
                lo=hi-1
                #bisect_right
                #item before hi< v3, item hi and after > =v3. when item(len-1) < v3, hi=len, lo=hi-1 always<len
                #check if lo>i+j+1 to prevent look back
                
                #bisect_left
                #item before lo< = v3, item lo and after > v3. when item(len-1) < v3, lo=len, hi=lo+1 will overflow
                # if use lo-1 would get duplicate idx (don't look back)
                
                if hi<len(nums) and abs(v3-nums[hi])<abs(diff):
                    diff=v3-nums[hi]
                if i+1+j<lo and abs(v3-nums[lo])<abs(diff):  
                    #when the value to compare is not the value to pass on
                    diff=v3-nums[lo]
                if diff==0:
                    break
        return target-diff

    #two pointer O(n^2)
    class Solution:
        def threeSumClosest(self, nums: List[int], target: int) -> int:
            n=len(nums)
            nums.sort()
            diff=float("inf")
            for i,v1 in enumerate(nums):
                lo=i+1
                hi=n-1
                while lo<hi:
                    test=v1+nums[lo]+nums[hi]
                    if abs(diff)>abs(target-test):
                        diff=target-test
                    if test==target:
                        return target
                    elif test<target:
                        lo+=1
                    else:
                        hi-=1
            return target-diff
        