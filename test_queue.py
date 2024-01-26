import my_queue as q

def test_enqueue():
    queue_instance = q.MyQueue(2)
    rear = queue_instance.enqueue(1)
    rear = queue_instance.enqueue(2)
    my_queue = queue_instance.getQueue()

    python_queue = []
    python_queue.append(1) 
    python_queue.append(2) 
    
    compare = (my_queue == python_queue)
    # Assert
    assert compare == True

def test_push_size():
    queue_instance = q.MyQueue(2)
    rear = queue_instance.enqueue(1)
    rear = queue_instance.enqueue(2)
    rear = queue_instance.enqueue(3)
    # Assert
    assert rear == -1


def test_dequeue():
    queue_instance = q.MyQueue(2)
    rear = queue_instance.enqueue(1)
    rear = queue_instance.enqueue(2)
    item = queue_instance.dequeue()

    my_queue = queue_instance.getQueue()
    my_queue = [1,2]
    item2 = my_queue.pop(0)
    
    # Assert
    assert item == item2

def test_dequeue():
    queue_instance = q.MyQueue(2)
    rear = queue_instance.enqueue(1)
    rear = queue_instance.enqueue(2)
    item = queue_instance.dequeue()
    item = queue_instance.dequeue()
    item = queue_instance.dequeue()

    # Assert
    assert item == -1

    

def test_circular():
    queue_instance = q.MyQueue(2)
    rear = queue_instance.enqueue(1)
    rear = queue_instance.enqueue(2)
    front = queue_instance.dequeue()
    # Assert
    assert front == 1
    assert rear == 1


def test_circular2():
    queue_instance = q.MyQueue(2)
    rear = queue_instance.enqueue(1)
    rear = queue_instance.enqueue(2)
    front = queue_instance.dequeue()
    rear = queue_instance.enqueue(3)
    front = queue_instance.dequeue()
    # Assert
    assert front == 2
    assert rear == 0
    

    

