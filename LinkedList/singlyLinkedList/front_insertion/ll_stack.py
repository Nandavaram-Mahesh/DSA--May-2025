from singly_linked_list_front import LinkedList
from stack_exception import StackUnderFlow , StackOverFlow, StackException



class Node:
    def __init__(self,data):
        self.data = data
        self.nextPtr = None
        
class Stack:
    def __init__(self,max_size):
        self.top =None
        self.size=0
        self.max_size = max_size
    
    
    def push(self,data):
        # Create New Node
        new_node = Node(data)
        # Check if stack is empty
        if self.top is None:
            self.top = new_node
            return
        # If stack is full raise StackOverFlow Error
        if self.size>=self.max_size:
            raise StackOverFlow("Stack is full!")

        new_node.nextPtr = self.top
        self.top = new_node
        self.size+=1
        return
    
    def pop(self):
        # check if stack is empty , if it is raise StackUnderFlowError
        if self.top is None:
            raise StackUnderFlow('Stack  is Empty')
        
        popped_data = self.top
        self.top = self.top.nextPtr
        self.size-=1
        return popped_data
    
    
    def display(self):
        temp = self.top
        while temp:
            print(f'Node Data:{temp.data}')
            temp = temp.nextPtr
        return     

# Client Code
stack = Stack(5)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.display()
        
        

