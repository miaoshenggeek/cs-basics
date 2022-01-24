from collections import defaultdict
from heapq import heappop, heappush
import math

#to reverse a list s
s=[0,1,2,3,4]
#s.reverse() #works #space O(1)
#s[:] = s[::-1] #works # Space O(n) 
s = s[::-1]
print(s)

x=2
a=math.ceil(math.sqrt(x))
b=int(math.sqrt(x))
c=math.floor(math.sqrt(x))
d=round(math.sqrt(x))
e=round(3.8)
f=round(3.4)
print(a,b,c,d,e,f)


astring="a little effort everyday is a great achievement in the long run"
print(astring.title())


st="0123"
two_digit = int(st[0: 3])
print(two_digit) #12 #int wull remove front 0

print(bin(1) + bin(1))
print(bin(1))

import random
#The only differences between randrange and randint that 
# randrange([start], stop[, step]) you can pass a step argument and random. 
# randrange(0, 1) will not consider the last item, 
# randint(0, 1) returns a choice inclusive of the last item.
print(random.randrange(3, 9))
print(random.randint(3,9))
#Return the next random floating point number in the range [0.0, 1.0)
print(random.random()*6+3)

#shallow copy doesn't work for nested list
"""
Techniques to deep copy: 
Using copy.deepcopy()
Techniques to shallow copy: 
Using copy.copy()
Using list.copy()
Using slicing"""

import copy
li1 = [1, 2, [3,5], 4]
# using deepcopy to deep copy 
li2 = copy.deepcopy(li1)
# using copy to shallow copy 
li2 = copy.copy(li1)

#turn 2D-List to Tuple so that hashable

res=[[0, 0], [0, 1], [1, 0]]
print(tuple(c for r in res for c in r))
print(c for r in res for c in r)

#enumerate(iterable, start=0)
print("enumerate")
rest=[0,1,1,1,0,0,1,1,0]
for i,v in enumerate(rest[1:]): #idx from 0-7, valuse as iterator
    print(i,v)
for i,v in enumerate(rest[1:],1): #idx from 1-8, value as same
    print(i,v)

h = []
heappush(h, (5, 'write code'))
heappush(h, (7, 'release product'))
heappush(h, (1, 'write spec'))
heappush(h, (1, 'write spec'))
heappush(h, (1, 'write'))
heappush(h, (1, 'aa'))
heappush(h, (3, 'create tests'))
while h:
    print(heappop(h))
"""# when tuple is pushed to heap, pop key is (tuple[0],tuple[1])
(1, 'aa')
(1, 'write')
(1, 'write spec')
(1, 'write spec')
(3, 'create tests')
(5, 'write code')
(7, 'release product')"""
class weight:
  def __init__(self, weight):
    self. weight= weight
  def __lt__(self,other):
    return self.weight>other.weight #flip < to >
a=weight(50)
b=weight(60)
print(a<b)

#counter is O(n) as it is implemented by dictionary
a = {} 
a = defaultdict(lambda:-1,a)
print("anything" in a) #=> False
print(a["anything"]) # => -1
print("anything" in a) #=> True
# for defaultdict, using index subscription creat the item by default
#b=defaultdict(a)  # TypeError: first argument must be callable or None
c=defaultdict(int)
print("q" in c) #=> False
print(c["q"]==0) # => True   # first argument is int set by default 0
print("q" in c) #=> True
print(a) #=> defaultdict(<function <lambda> at 0x0000012AD92CF280>, {'anything': -1})
print(c) #=> defaultdict(<class 'int'>, {'q': 0})

b=defaultdict()  #first argument is None 
print("d" in b) #=>False
#print(b["d"]) #keyError
b["d"]=1
b["2"]="d"
print (b) #=>defaultdict(None, {'d': 1, '2': 'd'})