#347.Given an integer array nums and an integer k,
# return the k most frequent elements. You may return the answer in any order.
import collections
from typing import Counter, DefaultDict, List
import heapq

#TO DO: quick select

class Solution:
    def topKFrequent(self, nums, k): #O(n)
        # bucket sort idea: no frequencies can be more than n
        bucket = [[] for _ in range(len(nums) + 1)] #看成按index排好序的hashmap
        Count = Counter(nums).items()  
        for num, freq in Count: 
            bucket[freq].append(num) 
        flat_list = [item for sublist in bucket for item in sublist]
        return flat_list[::-1][:k]
    
        # counter + heap - min heap
        # time: O(n + nlogk)
        # space: O(n)
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key = count.get)  #key =lambda i: count[i]
        
        def heapNlargest(num,k):# 2D heap [(2, 2), (3, 1)]
            heap = []
            for num, freq in count.items():
                if len(heap) < k or freq > heap[0][0]:
                    heapq.heappush(heap, (freq, num))
                if len(heap) > k:
                    heapq.heappop(heap)
            return [num for freq, num in heap]
    
    #bucket sort
    #TC: O(n)
    #TS: O(n)
    class Solution:
        def topKFrequent(self, words: List[str], k: int) -> List[str]:
            bucket=[[] for _ in range(len(words)+1)]  #each pair is count for each word
            c=collections.Counter(words)
            for word,count in c.items():
                bucket[count].append(word)
            res=[]
            for i,wordlist in enumerate(bucket[::-1]):
                res.extend(sorted(wordlist))#O(len(wordlist) log )
                if len(res)>=k:return res[:k]
            return res

    class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            dic=DefaultDict(list)
            for word in strs:
                key="".join(sorted(word))
                dic[key].append(word)
            return dic.values()
    #use bucket sort (constant) to reduce time for sort
    def groupAnagrams(self,strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()