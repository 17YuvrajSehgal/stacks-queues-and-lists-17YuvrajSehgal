# PRIORITY QUEUES
# Like an ordinary queue, a priority queue has a front and a rear, and items are removed from the front. 
# In a priority queue, however, each element has a priority value associated with it. 
# When you add an element to the queue, it is inserted in a position based on its priority value. Items are ordered by a priority value so that the item with the highest 
# priority (which in many implementations is the lowest value of a key) is always at the front. 
# When multiple items have the same priority, they follow the queue ordering, FIFO, so that the oldest inserted item comes first. 
# As with both stacks and queues, no access is provided to arbitrary items in the middle of a priority queue.

class MyItem :
    def __init__(self, value, priority):
        self.value= value
        self.priority = priority

    def getPriority(self):
        return self.priority
    
    def getValue(self):
        return self.value
    
class MyPriorityQueue(object):
    def __init__(self, size):          # Constructor
      self.__maxSize = size           # Size of array
      self.__que = [None] * size      # Queue stored as a list
      self.__nItems = -1               # no items in queue

    def getQueue(self):
        return self.__que
    
    # Exercise 05: implement a function that inserts item at rear of queue given its piority. 
    # Return the index to the item or -1 if the stack size has achieved its maximal size. 
    # (do not use any python built-in function)       
    def enqueue(self, item):     
        ''' Insert item at rear of the queue given the item priority'''        
        ## ADD YOUR CODE HERE
    
    # Exercise 06: implement a function that removes front item of queue. 
    # Return the item or -1 if the stack is empty. 
    #(do not use any python built-in function)  
    def dequeue(self):    
        '''Return front item of priority'''              
        ## ADD YOUR CODE HERE  
    
    
