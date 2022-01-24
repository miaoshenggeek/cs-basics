class Solution:
    def countKdivPairs(self, arr, n, k):
        #code here
        from collections import defaultdict
        if k==1:return n*(n-1)//2
        ct=0
        for i in range(n):
            arr[i]%=k
        
        dic=defaultdict(int)
        for i in range(n):
            v=(k-arr[i])%k     # to include 0
            if v in dic:
                ct+=dic[v]
            dic[arr[i]]+=1
        return ct