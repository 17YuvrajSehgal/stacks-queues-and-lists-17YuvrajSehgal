# A SIMPLE LINKED LIST
# In a linked list, each data item is embedded in a link. 
# A link represents one element of the overall list. 
# Each link holds some data and a way to get to the next link in the list.
import test_list


# The linked list has the following operations:
# - get and set methods for the first link,
# - add
# - remove
# - search


class MyListNode:
    def __init__(self, data, next=None):  # Constructor
        self.__data = data  # The data for this link
        self.__next = next  # Reference to next Link

    def getData(self):  # Return the datum stored in this link
        return self.__data

    def setData(self, data):  # Change the data in this Link
        self.__data = data

    def getNext(self):  # Return the next link
        return self.__next

    def setNext(self, link):  # Change the next link to a new Link
        if link is None or isinstance(link, MyListNode):  # Must be Node or None
            self.__next = link
        else:
            raise Exception("Next link must be Link or None")

    def isLast(self):  # Test if link is last in the chain
        return self.getNext() is None  # True if & only if no next Link

    def has_value(self, value):  # Compare the value with the node data
        if self.data == value:
            return True
        else:
            return False


class MyLinkedList(object):  # A linked list of data elements
    def __init__(self):  # Constructor
        self.__head = None  # Reference to first Link

    def getHead(self):
        return self.__head  # Return the first link

    def setHead(self, node):  # Change the first link to a new Link
        """Set the node as the head.
         Return -1 if node is not an instance of class ListNode"""
        ## ADD YOUR CODE HERE
        self.__head = node

    def isEmpty(self):
        """
        Returns true if  the Linked List is empty (e.g., None) or not
        """
        # we only have to check the head if is None or not
        ## ADD YOUR CODE HERE
        return self.__head == None

    def insert(self, data):  # insert the specified element to the head of this list.
        """
        Create a new node at the head of the Linked List
        """
        ## ADD YOUR CODE HERE
        node = MyListNode(data)
        node.setNext(self.__head)
        self.__head = node

    def remove(self):
        """
          Remove the first element (i.e., the head) of the Linked List
          Return -1 if list is empty,the data otherwise
          """
        ## ADD YOUR CODE HERE
        node = self.getHead()
        if (node is None):
            return -1
        self.__head = self.__head.getNext()
        return node.getData()

    def find(self, item):
        """
        Search for item in Linked List with data = item
        Return None if item not found, return the node otherwise
        """
        ## ADD YOUR CODE HERE
        node: MyListNode = self.getHead()
        while node is not None:
            if node.getData() == item:
                return node
            node = node.getNext()
        return None

    def getCount(self):  # Get length of list
        ## ADD YOUR CODE HERE
        counter = 0
        node: MyListNode = self.__head
        while (node is not None):
            counter = counter + 1
            node = node.getNext()
        return counter

    # Insert a new data after a given value
    def insertAt(self, goal, data):
        """
        Insert a new value AFTER the given value 'goal',
        Return false if value goal is not found and data cannot be insert
        Return true otherwise
        """
        ## ADD YOUR CODE HERE
        counter = 0
        node: MyListNode = self.__head
        newNode: MyListNode = MyListNode(data)
        while node is not None:
            if node.getData() == goal:
                newNode.setNext(node.getNext())
                node.setNext(newNode)
            node = node.getNext()

        return False

    def removeItem(self, item):
        """
        Remove node with value equal to item
        Return False if value is not found
        Return True otherwise
        """
    ## ADD YOUR CODE HERE
        prev = None
        node = self.getHead()
        while node is not None:
            # when node to be deleted is head
            if node.getData() == item and prev is None:
                self.setHead(node.getNext())
                return True
            # when node to be deleted is other node
            if node.getData() == item:
                prev.setNext(node.getNext())
                return True

            prev = node
            node = node.getNext()

        return False



def main():
    test_list.test_insert()
    test_list.test_empty1()
    test_list.test_empty2()
    test_list.test_head()
    test_list.test_count()
    test_list.test_insertAt()
    test_list.test_insertAt2()
    test_list.test_remove()
    test_list.test_find()
    test_list.test_find2()
    test_list.test_find3()
    test_list.test_removeItem()
    test_list.test_removeItem2()
    test_list.test_removeItem3()
    test_list.test_removeItem4()


if __name__ == '__main__':
    main()
