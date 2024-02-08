# PRIORITY QUEUES
# Like an ordinary queue, a priority queue has a front and a rear, and items are removed from the front. 
# In a priority queue, however, each element has a priority value associated with it. 
# When you add an element to the queue, it is inserted in a position based on its priority value. Items are ordered by a
# priority value so that the item with the highest
# priority (which in many implementations is the lowest value of a key) is always at the front. 
# When multiple items have the same priority, they follow the queue ordering, FIFO, so that the oldest inserted item comes first. 
# As with both stacks and queues, no access is provided to arbitrary items in the middle of a priority queue.
import test_pqueue


class MyItem:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def getPriority(self):
        return self.priority

    def getValue(self):
        return self.value


class MyPriorityQueue(object):
    def __init__(self, size):  # Constructor
        self.__maxSize = size  # Size of array
        self.__que = [None] * size  # Queue stored as a list
        self.__nItems = -1  # no items in queue

    def getQueue(self):
        return self.__que

    # Exercise 05: implement a function that inserts item at rear of queue given its piority.
    # Return the index to the item or -1 if the stack size has achieved its maximal size.
    # (do not use any python built-in function)
    def enqueue(self, item: MyItem):
        ''' Insert item at rear of the queue given the item priority'''
        ## ADD YOUR CODE HERE
        if self.__maxSize - 1 <= self.__nItems:
            return -1

        counter: int = 0
        for element in self.__que:
            # if priority is greater move all the elements to the right and insert at that place
            if element is None:
                self.__nItems += 1
                self.__que[self.__nItems] = item
                return self.__nItems
            elif element.getPriority() >= item.getPriority():
                counter += 1
            else:
                for i in range(self.__nItems + 1, counter, -1):
                    self.__que[i] = self.__que[i - 1]
                self.__que[counter] = item
                self.__nItems += 1
                return counter

    # Exercise 06: implement a function that removes front item of queue.
    # Return the item or -1 if the stack is empty. 
    # (do not use any python built-in function)
    def dequeue(self):
        '''Return front item of priority'''
        ## ADD YOUR CODE HERE
        if self.__nItems < 0:
            return -1
        item = self.__que[0]
        for i in range(0, self.__nItems):
            self.__que[i] = self.__que[i + 1]
        self.__nItems -= 1
        return item


def main():
    test_pqueue.test_enqueue()
    test_pqueue.test_enqueue_seq()
    test_pqueue.test_enqueue_size()
    # test_pqueue.test_dequeue()
    test_pqueue.test_dequeue2()


if __name__ == '__main__':
    main()
