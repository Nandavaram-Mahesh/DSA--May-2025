import sys
import os


project_root  = os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
print(f'Current_dir_name:{os.path.dirname(__file__)}')
print(f'project_root:{project_root}')
sys.path.append(project_root)

from LinkedList.singlyLinkedList.stack_exception import StackUnderFlow , StackOverFlow, StackException


# # we are going to implement stack using lists
# # Should i throw and error is the stack is full and empty ---> stakOverflow and StackUnderflow Errors

class Stack:
    
    def __init__(self,maxSize):
        self.stack =[]
        self.maxSize = maxSize
    
    # isEmpty
    def isEmpty(self):
        return len(self.stack)==0
    # isFull
    def isFull(self):
        # check if len(stack)>=maxSize 
        return len(self.stack)>=self.maxSize
            
    # push
    def push(self,data):
        # check if stack is full
        if self.isFull():
            raise StackOverFlow('Stack is Full')
        self.stack.append(data)
        return
    # pop
    def pop(self):
        # check if stack is empty
        if self.isEmpty():
            raise StackUnderFlow('Stack is empty')
        popped_data = self.stack.pop()
        return popped_data
    # peek
    def peek(self):
        # check the top element of the stack
        if self.isEmpty():
             raise StackUnderFlow('Stack is empty')
        return self.stack[-1]
    
    def empty_stack(self):
        self.stack.clear()
        return
    
    # display
    def display(self):
        for data in self.stack:
            print(data)
        return



stack = Stack(maxSize=5)

stack.empty_stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
# stack.push(6)



# stack.display()

# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()


stack_top_element = stack.peek()

print(f'stack_top_element:{stack_top_element}')

stack.display()

 
    
    
            