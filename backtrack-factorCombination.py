from math import sqrt
from typing import List

#254
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        
        res=[]
        def helper(target,ans=[],start=2):
            if len(ans)>0:
                res.append(ans+[target])
            for i in range(start,int(sqrt(target))+1):
                if target%i==0:
                    ans.append(i)
                    helper(target//i,ans,i)
                    ans.pop()
        helper(n)
        return res
    '''
        res = []
        def helper(prev_factor, arr, n):
            for i in range(prev_factor, int(math.sqrt(n))+1):
                if not n%i:
                    res.append(arr + [i, n//i])
                    helper(i, arr + [i], n//i)
        helper(2, [], n)
        return res  '''