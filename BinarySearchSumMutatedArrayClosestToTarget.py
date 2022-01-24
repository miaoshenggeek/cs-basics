from bisect import bisect_left
from typing import List

#1300
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        '''arr.sort()
        s, n = 0, len(arr)
        for i in range(n):
            # ans is best to replace everything from i and on. 
            ans = round((target - s)/n)   #use round to return closest integer to float-四舍五入
            # if this number is smaller than i-th number
            # then return this number, as the next one only makes it bigger
            if ans < arr[i]: return ans 
            s += arr[i]
            n -= 1
        return arr[-1]'''
        s = sorted(arr)
        l = len(s)
        total = 0
        for i in range(l):
            if total + s[i] * (l - i) >= target:
                predict = round((target - total) / (l - i))
                if abs(total + predict * (l - i) - target) == abs(total + (predict - 1) * (l - i) - target):
                    return predict - 1
                return predict
            total += s[i]
        return s[-1] 

class Solution(object):
    def getRes(self,arr,t):
        nums = [t if num >= t else num for num in arr]
        return sum(nums)
    
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        l = 1
        h = max(arr)
        
        while l <= h:
            mid = (h-l)//2 + l
            curr = self.getRes(arr,mid)
            if curr == target:
                return mid
            elif curr < target:
                l = mid+1
            else:
                h = mid-1
        #end loop l<h or l==h
        #either mid==h+1 or mid==l-1
        if abs(self.getRes(arr,l) - target) < abs(self.getRes(arr,h) - target):
            return l
        return h
    
    def findBestValue(self, arr: List[int], t: int) -> int:
        n=len(arr)
        arr.sort()
        ub=max(arr)
        lb=1
        while lb<ub:
            mid=lb+(ub-lb)//2
            a=bisect_left(arr,mid,0,n)
            can=sum(arr[:a])+mid*(n-a) #F(lb)
            if can==t:
                ub=mid  # return mid
            elif can<t:
                lb=mid+1 #
            elif can>t:
                ub=mid
        # end loop lb==ub
        # either lb==ub=mid (can>=t) or ub==lb=mid+1 (can<t for mid, while can>=t fot lb)
        # always return lb , F(lb)>=t
        # compare F(lb) with F(lb-1),where F(lb-1)<t
        a=bisect_left(arr,lb,0,n)
        can=sum(arr[:a])+lb*(n-a)
        b=bisect_left(arr,lb-1,0,n)
        can1=sum(arr[:b])+(lb-1)*(n-b)
        return lb if abs(can-t)<abs(can1-t) else lb-1