# QUEUES: 
# A Queue works on the principle of “First-in, first-out”. A queue has two simple operations:
# enqueue - It adds an element to the end of the queue.
# dequeue - It removes the element from the beginning of the queue.

class MyQueue(object):
    def __init__(self, size):          # Constructor
      self.__maxSize = size           # Size of [circular] array
      self.__que = [None] * size      # Queue stored as a list
      self.__rear = -1                # empty queue
      self.__front = 0                # Empty Queue has front 0
      self.__nItems = 0               # No items in queue
    
    def getQueue(self):
        return self.__que

    # Exercise 03: implement a function that inserts item at rear of queue.
    # Return the index to the item or -1 if the stack size has achieved its maximal size. 
    # (do not use any python built-in function)   
    def enqueue(self, item):         
        '''Insert item at rear of queue''' 
        ## ADD YOUR CODE HERE
    

    # Exercise 04: implement a function that removes front item of queue. 
    # Return the item or -1 if the stack is empty. 
    #(do not use any python built-in function)  
    def dequeue(self): 
        ''' Remove front item of queue'''                 
        ## ADD YOUR CODE HERE