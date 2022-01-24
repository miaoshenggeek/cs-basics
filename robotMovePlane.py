#1041. Robot Bounded In Circle
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirt=[[0,1],[1,0],[0,-1],[-1,0]] #north,left,south,right
        st,ed=0,0
        turn=0
        for i in instructions:
            if i=="G":
                st+=dirt[turn][0]
                ed+=dirt[turn][1]
            elif i=="L":
                turn+=3
                turn%=4
            else:
                turn+=1
                turn%=4
            
        return (not turn==0) or (st==0 and ed==0)