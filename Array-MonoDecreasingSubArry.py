from typing import List

#2110. Number of Smooth Descent Periods of a Stock
class Solution:
    def getDescentPeriods(self, p: List[int]) -> int:
        if len(p)==1:return 1
        stack=[p[0]]
        count=1
        res=1
        i=1
        while stack:
            prev=stack.pop()
            cur=p[i]
            if prev-cur==1:
                count+=1
                res+=count
            else:
                count=1
                res+=count
            if i< len(p)-1:stack.append(p[i])
            i+=1
        return res
        '''# use a param to record the maxiumum continuous descent days
        if len(p)==1:return 1
        stack=[p[0]]
        count=1
        res=1
        for i in p[1:]:
            if i==stack.pop()-1:
                count+=1
                res+=count
            else:
                count=1
                res+=count
            stack.append(i)
        return res       '''


#Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if n<=2:return 0
        #if height decrease then increase, there is a pit
        #if height keeps increasing or decreasing, no pit
        #if height increase then decrease, no pit
        #use stack to save strickly decreasing nums, when the next num increase, pop and count
        #when the next num stays same, renew the position of the bar
        
        start=height[0]
        stack=[(0,start)]
        res=0
        for i,v in enumerate(height):
            #print(stack)
            if v==start:
                stack.pop()
                stack.append((i,v))
            elif v<start:
                stack.append((i,v))
                start=v
            elif v>start and stack:
                base=stack.pop()[1]
                while stack and stack[-1][1]<=v:
                    h=stack[-1][1]-base
                    w=i-stack[-1][0]-1
                    res+=h*w
                    base=stack[-1][1]
                    stack.pop()
                    print(res)
                if stack and stack[-1][1]> v: 
                    res+=(v-base)*(i-stack[-1][0]-1)
                stack.append((i,v))
                start=v
                #print(res)
        return res
class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[]
        res=0
        n=len(height)
        for i,v in enumerate(height):
            while stack and stack[-1][1]<v:
                base=stack.pop()[1]
                h=min(stack[-1][1],v)-base if stack else 0
                w=i-stack[-1][0]-1 if stack else 0
                res+=h*w
            stack.append((i,v))
        return res
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if n<=2:return 0
        res=0
        l=0
        r=n-1
        lmax=height[l]
        rmax=height[r]
        while l<r:
            if height[l]<height[r]:
                l+=1
                lmax=max(height[l],lmax)
                if height[l]<lmax:
                    res+=lmax-height[l]
            else:
                r-=1
                rmax=max(height[r],rmax)
                if height[r]<rmax:
                    res+=rmax-height[r]
        return res
            
                    
        