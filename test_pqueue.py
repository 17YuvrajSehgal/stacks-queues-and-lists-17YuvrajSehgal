import my_priority_queue as q

def test_enqueue():
    queue_instance = q.MyPriorityQueue(2)
    item1 = q.MyItem(1, 0)
    item2 = q.MyItem(2, 1)
    rear = queue_instance.enqueue(item1)
    rear = queue_instance.enqueue(item2)
    my_queue = queue_instance.getQueue()

    py_queue = [item2,item1]
    # Assert
    assert my_queue == py_queue
    assert rear == 0

def test_enqueue_seq():
    queue_instance = q.MyPriorityQueue(3)
    item1 = q.MyItem(1, 0)
    item2 = q.MyItem(2, 1)
    item3 = q.MyItem(2, 0)
    rear1 = queue_instance.enqueue(item1)
    rear2 = queue_instance.enqueue(item2)
    rear3 = queue_instance.enqueue(item3)
    # Assert
    assert rear1 == 0
    assert rear2 == 0
    assert rear3 == 2

def test_enqueue_size():
    queue_instance = q.MyPriorityQueue(2)
    item1 = q.MyItem(1, 0)
    item2 = q.MyItem(2, 1)
    item3 = q.MyItem(2, 0)
    rear1 = queue_instance.enqueue(item1)
    rear2 = queue_instance.enqueue(item2)
    rear3 = queue_instance.enqueue(item3)
    # Assert
    # Assert
    assert rear3 == -1

def test_dequeue():
    queue_instance = q.MyPriorityQueue(2)
    item1 = q.MyItem(1, 0)
    item2 = q.MyItem(2, 1)
    queue_instance.enqueue(item1)
    queue_instance.enqueue(item2)
    
    item = queue_instance.dequeue()
    
    # Assert
    assert item.getValue() == item2.getValue()
    assert item.getPriority() == item2.getPriority()

def test_dequeue2():
    queue_instance = q.MyPriorityQueue(2)
    item1 = q.MyItem(1, 0)
    item2 = q.MyItem(2, 1)
    queue_instance.enqueue(item1)
    queue_instance.enqueue(item2)
    
    queue_instance.dequeue()
    queue_instance.dequeue()
    item = queue_instance.dequeue()
    
    # Assert
    assert item == -1




    


    

