import collections, heapq
from typing import List

#To customize python heap compare,Just wrap a class with customize compare function.
#Heap elements can be tuples. This is useful for assigning comparison values
#  (such as task priorities) alongside the main record being tracked:
class ReverseWordOrder:
    def __init__(self, word):
        self.word = word
    
    def __lt__(self, other):
        # guaranteed no equality since we are comparing keys in counter
        # flipping the lesser than comparator for our purpose to keep greater word in heap
        return self.word > other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)    # O(n) space and time
        #return heapq.nsmallest(k, counter, key=lambda word:(-counter[word], word))
        heap = []    # max length will be k, so O(k) extra space
        for word,freq in counter.items():    # O(n) time to iterate counter
            heapq.heappush(heap, (freq,ReverseWordOrder(word)))    # O(logk)
            if len(heap) > k:    # maintain the heap length of k
                heapq.heappop(heap)    # pop the smallest freq #O(log k)
        output = []    # O(k) space, same length as heap
        while heap:    # O(k) since len(heap) = k
            _freq, reverseWordObj = heapq.heappop(heap)    # O(logk)
            output.append(reverseWordObj.word)
        return output[::-1]    # O(k)
        #TC:O(n log k)
        #TS:O(n)
        #return heapq.nlargest(k, c.keys(), key = c.get)#no lexicographical sorting result
        # heapq.nsmallest(k, Freqs, key=lambda word:(-Freqs[word], word)
        # -Freqs[words] means 'rank the frequencies of words in descending order' 
        #(the first sorting criteria in lambda function);
        # word means 'rank the words with the highest frequencies in their alphabetical order'
        # (the second sorting criteria in lambda function).
        # Finally, nsmallest() returns the [:k] of the result.
        # nsmallest is implemented O(nlgk)# just maintains a heap size k, not n.

        #q.pop() pop from end, but the end is random, heapq.heappop(q) pop from head
        
        
        #bucket sort
        #TC: O(n)
        #TS: O(n)
        bucket=[[] for _ in range(len(words)+1)]  #each pair is count for each word
        c=collections.Counter(words)
        for word,count in c.items():
            bucket[count].append(word)
        res=[]
        for i,wordlist in enumerate(bucket[::-1]):
            res.extend(sorted(wordlist))#O(len(wordlist) log )
            if len(res)>=k:return res[:k]
        return res