class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        '''if not "0" in s or not "1" in s or len(s)==1: return 0
        n=len(s)
        P=[0]*(n+1)
        for i in range(n):
            P[i+1]=P[i]+int(s[i])
        #print(P)
        ans=n
        for i in range(n+1):
            ans=min(ans,n-i-(P[n]-P[i])+P[i])
        return ans'''

        #那我们只要一直记录着当前位置的前面有多少个1，后面有多少个0即可！
        #注意：可能存在最后全为0的情况（如示例3），那么我们是选不到某个’1’作为开头的，
        #所以我们先将全部翻转成’0’所花费的次数作为初始默认次数，然后和我们每次计算的结果比较即可。
        """n = len(s)
        cnt0 = s.count('0')
        cnt1 = 0
        res = n - cnt0
        for i in range(n):
            if s[i] == '0': 
                cnt0 -= 1
            elif s[i] == '1':
                res = min(res, cnt1+cnt0)
                cnt1 += 1
        return res"""
        

        ones = zeros = 0
        result = 0
        for c in s:
            if c == "1":
                ones += 1
            else:
                if ones: # 0s after 1s
                    zeros += 1
                    if zeros == ones:#A greedy approach: when more or equal 0s after 1s, flip 1s.
                        result += ones
                        ones = zeros = 0
        result += zeros
        return result
        