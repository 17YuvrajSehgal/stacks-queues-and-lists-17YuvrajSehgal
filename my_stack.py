# STACKS
# A stack data structure allows access to only one data item in the collection: the last item inserted.
# A Stack is a data structure that follows the LIFO(Last In First Out) principle.
import test_stack


# A stack has two simple operations:
# push - It adds an element to the top (i.e., end) of the stack.
# pop - It removes an element from the top (i.e, end) of the stack.

class MyStack(object):
    def __init__(self, max):           # Constructor
      self.__stackList = [None] * max  # The stack stored as a list
      self.__top = -1                  # No items initially
      self.__maxSize = max             # max Size of the stack   

    def getStack(self):
       return self.__stackList
    
    # Exercise 01: implement a function that inserts item at top of stack. 
    # Return the index to the item or -1 if the stack size has achieved its maximal size. (do not use any python built-in function)   
    def push(self, item): 
        '''Insert item at top of stack'''
        ## ADD YOUR CODE
        if self.__top >= self.__maxSize-1:
            return -1
        else:
            self.__top += 1
            self.__stackList[self.__top]=item
            return self.__top
        

    # Exercise 02: implement a function that removes the top item from stack. 
    # Return the item or -1 if the stack is empty. (do not use any python built-in function)   
    def pop(self):    
      '''Remove top item from stack'''
      ##ADD YOUR CODE
      if self.__top <= -1:
          return -1
      else:
          item = self.__stackList[self.__top]
          self.__stackList[self.__top] = None
          self.__top -=1
          return item

def main():
    test_stack.test_push()
    test_stack.test_pop_size()
    test_stack.test_pop_empty()
    test_stack.test_push_size()

if __name__ == "__main__":
    main()

