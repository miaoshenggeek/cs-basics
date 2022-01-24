#2135. Count Words Obtained After Adding a Letter
from typing import DefaultDict, List

"""#bit manupilation
reson fot bit mnp----No letter occurs more than once in any string of startWords or targetWords.
a binary encoding. ord returns the ascii number of the character ch. 
With 97, I assume that is the chr('a'). 
So, ord(ch) - 97 is returning an index according to the character. 
For 'a' returns 0, b returns 1, so on.
It's doing 1 << ord(ch) - 97 , so it's shifting the 1 by ord(ch)-97 positions. 
If ch is 'a', it will return 1. If ch is 'b', it will return 10, so on. 
If ch is a 'd' it will return 1000.
Notice that declared m = 0 and then, there is a loop that m ^= 1 << ord(ch) - 97
^ is the XOR operation that return 1 only when there is a 1 but not both. 
So, X XOR Y return 1 only if X = 1 or Y = 1 but no X =1 and Y = 1.
So, it's using the XOR to add the binary numbers. 
So, if it first encoded 'a', then m = 1 . 
Then, it's encoding 'b' , then m = m ^ 10, so m = 11 
(being 10 the 'b' encoding and m = 1 calculated in the previous iteration). So on.
This way, we can encode each word in a sequence of 0s and 1s. 
At the end, python converts the encoding to an integer. 
It will be a unique representation of each string."""
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        seen = set()
        for word in startWords: 
            m = 0
            for ch in word: m ^= 1 << ord(ch)-ord("a")
            seen.add(m)
            
        ans = 0 
        for word in targetWords: 
            m = 0 
            for ch in word: m ^= 1 << ord(ch) - ord("a")
            for ch in word: 
                if m ^ (1 << ord(ch)-ord("a")) in seen: #xor will elinimate ch from word each time
                    ans += 1
                    break 
        return ans 

    #bucketSort
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        
        def getHash(w: str) -> List[int]:
            h = [0] * 26
            for c in w:
                h[ord(c) - ord('a')] = 1
            return h
        
        groups = DefaultDict(set)  #set in dict
        for w in startWords:
            h = getHash(w)
            groups[len(w)].add(tuple(h))   # tuple is hashable
        cnt = 0
        for w in targetWords:
            h = getHash(w)
            for c in w:
                h[ord(c) - ord('a')] = 0
                if tuple(h) in (groups[len(w) - 1]):
                    cnt += 1
                    break
                h[ord(c) - ord('a')] = 1
        return cnt