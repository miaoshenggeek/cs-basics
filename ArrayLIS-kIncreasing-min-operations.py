from typing import List
from bisect import bisect_right

class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        l=len(arr)
        #Longest Increasing Subsequence//
        def LIS(lt):
            lis = []
            for x in lt:
                if not lis or lis[-1] <= x:
                    lis.append(x) # If num is greater than or equal to any element in sub
                else:
                    lis[bisect_right(lis, x)] = x # Otherwise, replace the first element in sub greater than num
            return len(lis)
        #k-partition, select one num from every k nums, cut array into K arrays
        res=0
        for i in range(0,k):
            newarr=[]
            for j in range(i,l,k):
                newarr.append(arr[j])
            #print(newarr)
            res+=len(newarr)-LIS(newarr)
                      
        return res
            
"""
[12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3]
1
[4,1,5,2,6,2]
2
[12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3]
11
"""