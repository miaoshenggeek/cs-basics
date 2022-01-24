from typing import List
import heapq
#sort the courses by endtime from end earliest to end latest
#use heapq to heapify duration, increment sum-duration to mark the current time
# if come across shorter time-comsumption in the future, 
# heappop and adjust the current time and then heappush the shorter duration.len of heapq is #of courses
# Time O(n log n) 
# loop through n elements, each element is heapified takes O (log n)
# Space O (n) at most n elements in heap
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda i: i[1])
        print(courses)
        alist=[]
        heapq.heapify(alist)
        
        #print(list(heapq)) #None
        time=0
        for dur,ddl in courses:
            if time+dur<=ddl:
                heapq.heappush(alist,dur)
                time+=dur
            elif alist and alist[0]>dur:
                time+=dur-heapq.heappop(alist)
                heapq.heappush(alist,dur)
        return len(alist)
#253. Meeting Rooms II
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals, key=lambda i: i[0])
        #print(intervals)
        l=len(intervals)
        queue=[]
        queue.append(intervals[0][1])
        #print(queue)
        for i in range(1,l):
            
            if intervals[i][0]>=min(queue):
                queue.remove(min(queue))
                #print(queue)
            queue.append(intervals[i][1])
            
        return len(queue)