from stack_exception import StackException,StackOverFlow,StackUnderFlow

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self,max_size):
        self.top=None
        self.size=0
        self.max_size=max_size
    # check if stack is empty
    def is_empty(self):
        return self.top is None
    # Push the elements to the stack
    def push(self,value):
        
        # If stack is full then raise StacckOverFlow Exception
        if self.size>=self.max_size:
            raise StackOverFlow("Stack is full!")
        # Else create a new node , point the new node to the top pointer and then shift the top pointer to new_node and then increment the seize
        new_node = Node(value)
        new_node.next=self.top
        self.top=new_node
        self.size+=1
        return 
    # Pop the elements from the stack
    def pop(self):
        if self.is_empty():
            raise StackUnderFlow("Stack is empty!")
        
        popped_data=self.top
        self.top=self.top.next
        self.size-=1
        return popped_data
    # Peek the elements from the stack
    def peek(self):
        if self.is_empty():
            raise StackUnderFlow("Stack is empty!")
        return self.top.data
    
    # display the stack elements
    def display(self):
        temp = self.top
        while temp:
            print(temp.data)
            temp=temp.next
        return 



try:
    new_stack = Stack(5)
    
    new_stack.push(10)
    new_stack.push(20)
    new_stack.push(30)
    new_stack.push(40)
    new_stack.push(50)
    new_stack.push(60)
    
    new_stack.display()
except StackException as e:
    print(e)    

