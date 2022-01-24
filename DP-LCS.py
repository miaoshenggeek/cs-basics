from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        '''# LCS
        #dp[i][j] will be the answer for inputs A[i:], B[j:].
        n=len(nums1)
        m=len(nums2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
        #print(dp)
        return max(j for i in dp for j in i)'''
        nums2Str = ''.join([chr(n) for n in nums2])
        longest = 0
        maxStr = ''
        for n in nums1:
            maxStr += chr(n)
            if maxStr in nums2Str:
                longest = max(longest, len(maxStr))
            else:
                maxStr = maxStr[1:]
        return longest
        
        #Rolling Hash