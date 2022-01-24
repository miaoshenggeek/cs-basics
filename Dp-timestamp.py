from typing import List

#2136. Earliest Possible Day of Full Bloom
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        z=list(zip(plantTime,growTime))
        z.sort(key=lambda i:-i[1]) 
        #sort by grow time descending,so longest grow time goes first
        rt=0
        start_time=0
        for p,g in z:
            start_time+=p  #timestamp
            rt=max(rt,start_time+g)
        return rt

#1094. Car Pooling
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        timestamp=[]
        for i,j,k in trips:
            timestamp.append([j,i])
            timestamp.append([k,-i])
        timestamp.sort()
        cur=0
        for i,j in timestamp:
            cur+=j
            if cur>capacity:return False
        return True'''
        
        #bucket sort
        ts=[0]*1001   #1 <= trips.length <= 1000 ts is the timestamp 
        for i,j,k in trips:
            ts[j]+=i
            ts[k]-=i
        cur=0
        for j in ts:
            cur+=j
            if cur>capacity:return False
        return True
        
    """
    [[2,1,5],[3,3,7]]
    4
    [[2,1,5],[3,3,7]]
    5
    [[8,2,3],[4,1,3],[1,3,6],[8,4,6],[4,4,8]]
    12
    [[1,1,4],[9,4,9],[9,1,9],[2,3,5],[4,1,5],[10,4,5]]
    33
    [[4,2,3],[2,3,9],[9,7,9],[10,2,9],[7,1,8],[6,2,5],[3,5,7],[2,2,5]]
    30
    [[9,3,6],[8,1,7],[6,6,8],[8,4,9],[4,2,9]]
    28"""