from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.d={}
        self.count=0
        self.history=deque()
        self.capacity=capacity

    def get(self, key: int) -> int:
        
        if key in self.d:
            self.history.remove(key)
            self.history.append(key)
            return self.d[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.count>=self.capacity and key not in self.d:
            temp=self.history.popleft()
            del self.d[temp]
        if key not in self.d:
            self.count+=1
            self.history.append(key)
        else:
            self.history.remove(key)
            self.history.append(key)
        self.d[key]=value
    
from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key]=value
        if len(self)>self.capacity:
            self.popitem(last=False)


#One advantage of double linked list is that the node can remove itself without other reference. 
# In addition, it takes constant time to add and remove nodes from the head or tail.
#One particularity about the double linked list implemented here is that 
# there are pseudo head and pseudo tail to mark the boundary, 
# so that we don't need to check the null node during the update.

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class DLinkedNode():
    def __init__(self):
        self.key=0
        self.value=0
        self.prev=None
        self.next=None
        
class LRUCache():
    def _add_node(self,node):  #add to head
        node.prev =self.head
        node.next =self.head.next
        self.head.next.prev =node
        self.head.next=node
        
    def __init__(self,capacity):
        self.cache={}
        self.size=0
        self.capacity =capacity
        self.head, self.tail =DLinkedNode(),DLinkedNode()
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def _remove_node(self,node):
        prev=node.prev
        new=node.next
        
        prev.next=new
        new.prev=prev
        
    def _move_to_head(self,node):
        self._remove_node(node)
        self._add_node(node)
        
    def _pop_tail(self):   #pop from tail
        res=self.tail.prev   
        self._remove_node(res)
        return res
        
    
    def get(self,key):
        node=self.cache.get(key,None) #
        if not node:
            return -1
        self._move_to_head(node)
        return node.value
    
    def put(self,key,value):
        node=self.cache.get(key) #
        if not node:
            newNode=DLinkedNode()
            newNode.key=key  #
            newNode.value=value  #
            self.cache[key]=newNode ####
            self._add_node(newNode)  ###
            self.size+=1
            if self.size>self.capacity:
                tail=self._pop_tail()
                del self.cache[tail.key]
                self.size-=1
        else:
            node.value=value
            self._move_to_head(node)
