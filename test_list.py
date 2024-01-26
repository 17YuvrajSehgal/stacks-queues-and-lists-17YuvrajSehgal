import my_linked_list as ll

def test_head():
    llist = ll.MyLinkedList()
    node1 = ll.MyListNode(1)
    llist.setHead(node1)

    assert llist.getHead().getData() == 1

def test_insert():
    llist = ll.MyLinkedList()

    llist.insert(1)
    llist.insert(2)
    llist.insert(3)

    assert llist.getHead().getData() == 3

def test_empty1():
    llist = ll.MyLinkedList()

    assert llist.isEmpty() == True

def test_empty2():
    llist = ll.MyLinkedList()
    node1 = ll.MyListNode(1)
    llist.setHead(node1)

    assert llist.isEmpty() == False

def test_insertAt():
    llist = ll.MyLinkedList()

    llist.insert(1)
    llist.insert(2)
    llist.insertAt(1, 3)

    assert llist.getHead().getData() == 2

def test_count():
    llist = ll.MyLinkedList()
    llist.insert(1)
    llist.insert(2)
    llist.insertAt(1, 3)


    assert llist.getCount() == 3

def test_remove():
    llist = ll.MyLinkedList()
    llist.insert(1)
    llist.insert(2)
    llist.insertAt(1, 3)

    data = llist.remove()

    assert data == 2

def test_removeItem():
    llist = ll.MyLinkedList()
    llist.insert(1)
    llist.insert(2)
    llist.insertAt(1, 3)


    data = llist.removeItem(1)

    assert data == True

def test_removeItem2():
    llist = ll.MyLinkedList()
    llist.insert(1)
    llist.insert(2)
    llist.insertAt(1, 3)


    data = llist.removeItem(4)

    assert data == False










    


    

