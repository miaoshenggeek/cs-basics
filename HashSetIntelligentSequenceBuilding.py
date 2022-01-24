from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:return n
        ns=set(nums)
        ans=0
        for num in ns:
            cnt=0
            if num-1 not in ns:
                cur=num
                cnt=1
                while cur+1 in ns:
                    cnt+=1
                    cur+=1
            ans=max(ans,cnt)
        return ans