class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":return 0
        if haystack=="":return -1
        #Using memoryview to slice without copying
        haystack = memoryview(bytes(haystack, 'ascii'))
        needle = memoryview(bytes(needle, 'ascii'))
        # slicing lists has a time-complexity of O(k), where "k" is the length of the slice
        m=len(needle)
        n=len(haystack)
        for i in range(n):
            if haystack[i:i+m]==needle:return i
        return -1