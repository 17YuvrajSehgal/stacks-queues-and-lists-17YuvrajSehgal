# A SIMPLE LINKED LIST
# In a linked list, each data item is embedded in a link. 
# A link represents one element of the overall list. 
# Each link holds some data and a way to get to the next link in the list.

#The linked list has the following operations:
#- get and set methods for the first link, 
#- add
#- remove
#- search 

   
class MyListNode:
    def __init__(self, data, next=None): # Constructor
        self.__data = data      # The data for this link
        self.__next = next      # Reference to next Link

    def getData(self):          # Return the datum stored in this link
        return self.__data

    def setData(self, data):   # Change the data in this Link
        self.__data = data

    def getNext(self): # Return the next link
        return self.__next 

    def setNext(self, link):    # Change the next link to a new Link
        if link is None or isinstance(link, MyListNode): #Must be Node or None
            self.__next = link
        else:
            raise Exception("Next link must be Link or None")

    def isLast(self):   # Test if link is last in the chain
        return self.getNext() is None  # True if & only if no next Link

    def has_value(self, value): # Compare the value with the node data
        if self.data == value:
            return True
        else:
            return False
    


class MyLinkedList(object):           # A linked list of data elements
    def __init__(self):             # Constructor
        self.__head = None          # Reference to first Link

    def getHead(self): return self.__head # Return the first link
    
    def setHead(self, node):        # Change the first link to a new Link
        """Set the node as the head.
         Return -1 if node is not an instance of class ListNode"""
        ## ADD YOUR CODE HERE

    def isEmpty(self):
        """
        Returns true if  the Linked List is empty (e.g., None) or not
        """
        #we only have to check the head if is None or not
        ## ADD YOUR CODE HERE
   
    def insert(self, data):    # insert the specified element to the head of this list. 
        """
        Create a new node at the head of the Linked List
        """ 
        ## ADD YOUR CODE HERE
    
    def remove(self):  
      """
        Remove the first element (i.e., the head) of the Linked List
        Return -1 if list is empty,the data otherwise
        """     
      ## ADD YOUR CODE HERE
    
    
    def find(self, item):
        """
        Search for item in Linked List with data = item
        Return None if item not found, return the node otherwise
        """
        ## ADD YOUR CODE HERE

    def getCount(self):          # Get length of list
        ## ADD YOUR CODE HERE
        return

    # Insert a new data after a given value
    def insertAt(self, goal, data):
        """
        Insert a new value AFTER the given value 'goal', 
        Return false if value goal is not found and data cannot be insert
        Return true otherwise
        """
        ## ADD YOUR CODE HERE
    

    def removeItem(self, item):  
        """
        Remove node with value equal to item
        Return False if value is not found
        Return True otherwise
        """  
        ## ADD YOUR CODE HERE
   

   

   
