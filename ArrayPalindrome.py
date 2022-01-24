from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def checkPan(w):
            s=1
            e=len(w)-2
            while s<e:
                if w[s]!=w[e]:
                    return False
                s+=1
                e-=1
            return True
        for i in words:
            if len(i)==1 or i[0]==i[-1] and checkPan(i):
                return i
        return 
    """#palindrome///
        for s in words:
                if s == s[::-1]:
                    return s
            return """