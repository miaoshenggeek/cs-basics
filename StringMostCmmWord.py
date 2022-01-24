from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words=[]
        cur=""
        for i in paragraph+" ":
            if i.isalpha():
                cur+=i
            else:
                if cur:words.append(cur.lower())
                cur=""
        banned = set(banned)
        ### method how to parse sentence with diff punctuations.
        # for c in "!?',;.":
        #     paragraph = paragraph.replace(c, " ")
        # paragraph = paragraph.lower().split()
        # str.lower() can work on sentence with non-alpha chars
        # normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

        c=Counter(words)
        for i in banned:
            del c[i]
        return max(c,key=lambda i: c[i])#  return max(dictname, key=dictname.get)
        ## method return max from a dict

        """
        setdefault in dict and augument 
        words={} or dict()
        words.setdefault(cur,0)
        words[cur]+=1"""