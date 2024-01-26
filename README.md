[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/iOPP1Mqx)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=13571758&assignment_repo_type=AssignmentRepo)
# PRACTICAL ASSIGNMENT 02: STACKS, QUEUES, LINKED LISTS

In this assignment you will implement:
- A simple stack
- Queue
- Priority queue
- Linked lists

## STACKS
A stack data structure allows access to only one data item in the collection: the last item inserted. A Stack is a data structure that follows the LIFO (Last In First Out) principle. 

A stack has two simple operations:
push: it adds an element to the top (i.e., end) of the stack.
pop: it removes an element from the top (i.e, end) of the stack.

Exercise 01: implement a function that inserts item at top of stack. Return the index to the item or -1 if the stack size has achieved its maximal size. (do not use any python built-in function)   

Exercise 02: implement a function that removes the top item from stack. Return the item or -1 if the stack is empty. (do not use any python built-in function)   
    
## QUEUES
A Queue works on the principle of “First-in, first-out”. A queue has two simple operations:
enqueue: it adds an element to the end of the queue.
dequeue: it removes the element from the beginning of the queue.

Exercise 03: implement a function that inserts item at rear of queue. Return the index to the item or -1 if the stack size has achieved its maximal size. (do not use any python built-in function)  
    
Exercise 04: implement a function that removes front item of queue.Return the item or -1 if the stack is empty. (do not use any python built-in function)  

## PRIORITY QUEUES
Like an ordinary queue, a priority queue has a front and a rear, and items are removed from the front. In a priority queue, however, each element has a priority value associated with it. When you add an element to the queue, it is inserted in a position based on its priority value. Items are ordered by a priority value so that the item with the highest  priority (which in many implementations is the lowest value of a key) is always at the front. 

When multiple items have the same priority, they follow the queue ordering, FIFO, so that the oldest inserted item comes first. As with both stacks and queues, no access is provided to arbitrary items in the middle of a priority queue.

Exercise 05: implement a function that inserts item at rear of queue given its priority. Return the index to the item or -1 if the stack size has achieved its maximal size. (do not use any python built-in function)       
    
Exercise 06: implement a function that removes front item of queue. Return the item or -1 if the stack is empty. (do not use any python built-in function)  

## A SIMPLE LINKED LIST
In a linked list, each data item is embedded in a link. A link represents one element of the overall list. Each link holds some data and a way to get to the next link in the list.

The linked list has the following operations: get, add, remove, and search 

Exercise 07: Set a node as the head of the list.

Exercise 08: Check if a linked list is empty

Exercise 09:Create a new node at the head of the Linked List

Exercise 10: Remove the first element (i.e., the head) of the Linked List

Exercise 11: Search for item in Linked List w

Exercise 12: Get length of list

Exercise 13: Insert a new data after a given value

Exercise 14: Remove node with value equal to item
        
   