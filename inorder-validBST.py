import math
from typing import List
class node:
     def __init__(self, data=0, left=None, right=None):
         self.data = data
         self.left = left
         self.right = right

def isValidBST(root:List[node]):
    stack=[]
    prev=-math.inf
    while stack and root:
        while root:
            stack.append(root)
            root=root.left
        root=stack.pop()
        if root.data<=prev:return False
        prev=root.data
        root=root.right
    return True

# Program for linked implementation
# of complete binary tree
 
# For Queue Size
SIZE = 50
 
 
# A queue node
class Queue:
     
    def __init__(self):
       
        self.front = None
        self.rear = None
        self.size = 0
        self.array = []
 
# A utility function to
# create a new tree node
def newNode(data):
     
    temp = node(data)
    return temp
 
# A utility function to
# create a new Queue
def createQueue(size):
     
    global queue   
    queue = Queue()
    queue.front = queue.rear = -1
    queue.size = size
    queue.array = [None for i in range(size)]
    return queue
     
# Standard Queue Functions
def isEmpty(queue):
 
    return queue.front == -1
 
def isFull(queue):
     
    return queue.rear == queue.size - 1
 
def hasOnlyOneItem(queue):
     
    return queue.front == queue.rear
 
def Enqueue(root):
 
    if (isFull(queue)):
        return
     
    queue.rear+=1
    queue.array[queue.rear] = root
 
    if (isEmpty(queue)):
        queue.front+=1
 
def Dequeue():
 
    if (isEmpty(queue)):
        return None
 
    temp = queue.array[queue.front]
 
    if(hasOnlyOneItem(queue)):
        queue.front = queue.rear = -1
    else:
        queue.front+=1
 
    return temp
 
def getFront(queue):
     
    return queue.array[queue.front]
 
# A utility function to check
# if a tree node has both left
# and right children
def hasBothChild(temp):
 
    return (temp and temp.left and
            temp.right)
     
# Function to insert a new
# node in complete binary tree
def insert(root, data, queue):
 
    # Create a new node for
    # given data
    temp = newNode(data)
 
    # If the tree is empty,
    # initialize the root
    # with new node.
    if not root:
        root = temp
    else:
     
        # get the front node of
        # the queue.
        front = getFront(queue)

        # If the left child of this
        # front node doesn’t exist,
        # set the left child as the
        # new node
        if (not front.left):
            front.left = temp
 
        # If the right child of this
        # front node doesn’t exist, set
        # the right child as the new node
        elif (not front.right):
            front.right = temp
 
        # If the front node has both the
        # left child and right child,
        # Dequeue() it.
        if (hasBothChild(front)):
            Dequeue()
 
    # Enqueue() the new node for
    # later insertions
    Enqueue(temp)
    return root
  
# Standard level order
# traversal to test above
# function
def levelOrder(root):
 
    queue = createQueue(SIZE)
    Enqueue(root)
     
    while (not isEmpty(queue)):   
        temp = Dequeue();        
        print(temp.data, end = ' ')
        if (temp.left):
            Enqueue(temp.left)
        if (temp.right):
            Enqueue(temp.right)
 
# Driver code 
if __name__ == "__main__":
     
    root = None
    queue = createQueue(SIZE)
     
    for i in range(1, 18):
        root=insert(root, i,queue)
      
    levelOrder(root)
    print(isValidBST(root))

