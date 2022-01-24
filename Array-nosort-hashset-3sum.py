#no sort TimeO(n^2)  Space O(n)
from typing import Counter, List
from bisect import bisect_left

#no sort put a combination of three values into a hashset to avoid duplicates
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()             #O(1)
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    val3 = -val1 - val2
                    if val3 in seen and seen[val3] == i:#i is to mark val1
                        res.add(tuple(sorted((val1, val2, val3))))          #O(1)
                    seen[val2] = i
        return res

#sort+two pointer
class Solution:     
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums==[] or len(nums)<3: return []        
        res=[]
        nums.sort()
        n=len(nums)        
        for i in range(n):
            pivot=nums[i]
            if pivot>0: break
            #to pass duplicate
            if i == 0 or nums[i - 1] != nums[i]:
                l=i+1
                r=n-1
                while l<r:
                    s=pivot+nums[l]+nums[r]
                    if s<0:
                        l+=1
                    elif s>0:
                        r-=1
                    else:
                        res.append([pivot,nums[l],nums[r]])
                        l+=1
                        r-=1
                        #to pass duplicates
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
        return res
    


#sort and turn to 2sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:#pass duplicate
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1
#binary search
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        freq = Counter(nums)
        #print(freq)
        nums = sorted(freq)
        #print(nums)
        if nums[0] > 0 or nums[-1] < 0: return []
        res = []
        for i, n in enumerate(nums):
            if -2 * n in freq and (freq[n] > 2 or (n and freq[n] > 1)):
                res.append((n, n, -2 * n))
            l = bisect_left(nums, -n - nums[-1], i + 1)
            r = bisect_left(nums, -n / 2, l)
            res.extend((n, m, -n - m) for m in nums[l:r] if -n - m in freq)

        return res