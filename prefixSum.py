from collections import defaultdict
from typing import DefaultDict, List

#560
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        dic=DefaultDict(int) #count=collections.Counter(), count[0]=1
        dic[0]=1
        cursum=0
        for i in nums:
            cursum+=i
            count+=dic[cursum-k]
            dic[cursum]+=1    #prefix sum
        return count
        
    def subarraySum(self, nums: List[int], k: int) -> int:
            dp=[0]#prefixSum
            cur=0
            for i in nums:
                cur+=i
                dp.append(cur)
            res=0
            #print(dp)
            dic=defaultdict(int) #2sum ->prev+k=i -> i-prev=k
            for i in dp:
                res+=dic[i-k] # i-(i-k)=k, i-k is prefix of i
                dic[i]+=1
            return res