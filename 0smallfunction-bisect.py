from bisect import bisect_left,bisect_right
from typing import List
#use in 2D array
data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
data.sort(key=lambda r: r[1])       # Or use operator.itemgetter(1).
keys = [r[1] for r in data]         # Precompute a list of keys.
print(data,keys)
data[bisect_left(keys, 0)]
('black', 0)
data[bisect_left(keys, 1)]
('blue', 1)
data[bisect_left(keys, 5)]
('red', 5)
data[bisect_left(keys, 8)]
('yellow', 8)

#when to choose bisect_right
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
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
                    diff=v3-nums[lo]
                if diff==0:
                    break
        return target-diff
        