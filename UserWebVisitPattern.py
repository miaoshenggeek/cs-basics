from collections import Counter, defaultdict
import itertools
from typing import List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        def combinations(l):
            for a in range(len(l)-2):
                for b in range(a+1,len(l)-1):
                    for c in range(b+1,len(l)):
                        yield (l[a],l[b],l[c])
        myDict=defaultdict(list)
        for u,t,w in sorted(zip(username,timestamp,website)):
            myDict[u].append(w)
        freq=Counter()
        for web_list in myDict.values():
            freq.update(set(combinations(web_list)))
        return min(freq, key=lambda x: (-freq[x],x))

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        arr=sorted(list(zip(username,timestamp,website))) #key is by default x[0],x[1],x[2]
        #print(arr)
        
        user=arr[0][0]
        start=0
        pattern=[]  # can also use defaultdict
        cur=[]
        while start<len(arr):
            if arr[start][0]==user:
                cur.append(arr[start][2])
            if not arr[start][0]==user or start==len(arr)-1:
                if len(cur)>=3:
                    pattern.append(cur)   
                user=arr[start][0]
                cur=[arr[start][2]]
            start+=1
        res=[]
        #print(pattern)
        for cur in pattern:
            if len(cur)>3:
                temp=set(itertools.combinations(cur,3))  
                #generate all combinations with 3 items,with same relative order
                res.extend(list(temp))
            else:
                res.append(tuple(cur))
        #print(res)
        if len(res)==1:return res[0]
        c=Counter(tuple(res))
        #print(c)
        return min(c.items(),key=lambda i:(-i[1],i[0]))[0]