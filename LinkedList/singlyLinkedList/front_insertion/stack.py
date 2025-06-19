from singly_linked_list_front import LinkedList
from stack_exception import StackUnderFlow , StackOverFlow, StackException



class Stack:
    def __init__(self,max_size):
        self.stack = LinkedList()
        self.size=0
        self.max_size = max_size
    
    
    def push(self,value):
        if self.size>=self.max_size:
            raise StackOverFlow("Stack is full!")
        self.stack.insert_at_front(value)
        self.size+=1
    
    def pop(self):
        self.stack.delete_at_front()
        self.size-=1
        

