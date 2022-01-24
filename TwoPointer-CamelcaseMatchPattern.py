from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        '''def helper(i):
            q=0
            p=0
            if len(i)<len(pattern):return False
            while q<len(i):
                if i[q]==pattern[p]:
                    if p==len(pattern)-1:return i[q+1:].islower() or q==len(i)-1
                    q+=1
                    p+=1
                elif i[q]!=pattern[p] and i[q].islower():
                    q+=1
                else:
                    return False
            return i[-1]==pattern[-1] 
                
        res=[]
        for i in queries:
            res.append(helper(i))
        return res'''
        #//method two pointers both from left, for loop can reduce extra work to increment one pointer
        def patternMatch(p: str, q: str) -> bool:
            i = 0
            for j, c in enumerate(q):
                if i < len(p) and p[i] == c:
                    i += 1
                elif c.isupper():
                    return False  
            return i == len(p)
        
        return [patternMatch(pattern, q) for q in queries]
                    