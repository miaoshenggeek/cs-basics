from typing import List

#1588
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        for window_size in range(1, len(arr)+1, 2):
            sumOfGivenWindow = 0
            for i in range(len(arr)-window_size+1):
                sumOfGivenWindow += sum(arr[i:i+window_size])
            total += sumOfGivenWindow
        return total
        
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        res=0
        for i in range(n):
            for j in range(0,n-i,2):
                res+=sum(arr[i:i+j+1])
        return res
            