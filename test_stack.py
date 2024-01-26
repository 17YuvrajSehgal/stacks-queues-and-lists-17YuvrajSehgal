import my_stack as st

def test_push():
    stack_instance = st.MyStack(2)
    stack_instance.push(1)
    stack_instance.push(2)
    my_stack = stack_instance.getStack()

    python_stack = []
    python_stack.append(1) 
    python_stack.append(2) 
    
    compare = (my_stack == python_stack)
    # Assert
    assert compare == True

def test_push_size():
    stack_instance = st.MyStack(3)
    top = stack_instance.push(1)
    top = stack_instance.push(2)
    top = stack_instance.push(3)
    top = stack_instance.push(4)

    # Assert
    assert top == -1

def test_pop_size():
    stack_instance = st.MyStack(2)
    top = stack_instance.push(1)
    top = stack_instance.push(2)
    top = stack_instance.pop()
    top -=1
    
    my_stack = [1,2]
    my_stack.pop()
    size = len(my_stack)
    
    # Assert
    assert top == 1
    assert top == size

def test_pop_empty():
    stack_instance = st.MyStack(3)
    stack_instance.push(1)
    top = stack_instance.pop()
    top = stack_instance.pop()
    # Assert
    assert top == -1

    

