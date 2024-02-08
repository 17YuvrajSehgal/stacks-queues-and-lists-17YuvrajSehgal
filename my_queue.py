# QUEUES: 
# A Queue works on the principle of “First-in, first-out”. A queue has two simple operations:
# enqueue - It adds an element to the end of the queue.
# dequeue - It removes the element from the beginning of the queue.
import test_queue


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
        if self.__maxSize <= self.__nItems:
            return -1
        else:
            self.__rear = (self.__rear+1) % self.__maxSize
            if self.__que[self.__rear] is None:
                self.__que[self.__rear]=item
                self.__nItems+=1
                return self.__rear



    # Exercise 04: implement a function that removes front item of queue. 
    # Return the item or -1 if the stack is empty. 
    #(do not use any python built-in function)  
    def dequeue(self): 
        ''' Remove front item of queue'''                 
        ## ADD YOUR CODE HERE
        if self.__nItems==0:
            return -1
        else:
            item = self.__que[self.__front]
            self.__que[self.__front]=None
            self.__front+=1
            self.__nItems-=1
            return item


def main():
    test_queue.test_enqueue()
    test_queue.test_dequeue()
    test_queue.test_dequeue2()
    test_queue.test_push_size()
    test_queue.test_circular()
    test_queue.test_circular2()

if __name__ == "__main__":
    main()