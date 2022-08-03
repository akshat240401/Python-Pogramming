#Stack can be implemented using List, Dequeue, and Queue method
#Append and Pop  are used to insert and delete elements from stack
#Stack followss LIFO approach

#LIST APPROACH
stack=[]
stack.append("Hello")
stack.append("Welcome")
stack.append("All")
print(stack)
print(stack.pop())

#DEQUEUE APPROACH
#Append and Pop operations are much quicker as compared to list
from collections import deque
from sys import maxsize
stack1=deque()
stack1.append("Hello")
stack1.append("Welcome")
stack1.append("All")
print(stack1)
print(stack1.pop())

#QUEUE APPROACH
# get()
# maxsize()
# empty()
# full()
# put(x)
# qsize()
from queue import LifoQueue
stack2=LifoQueue()(maxsize=3)
stack2.put(1)
stack.put(2)
stack2.put(3)
print (stack2)
print(stack2.qsize())
print(stack2.get())
print(stack2.qsize())