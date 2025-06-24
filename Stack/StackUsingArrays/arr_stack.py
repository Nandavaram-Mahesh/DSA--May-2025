import sys
import os


project_root  = os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
print(f'Current_dir_name:{os.path.dirname(__file__)}')
print(f'project_root:{project_root}')
sys.path.append(project_root)

from LinkedList.singlyLinkedList.container_exception import containerUnderFlow , containerOverFlow, containerException


# # we are going to implement container using lists
# # Should i throw and error is the container is full and empty ---> stakOverflow and containerUnderflow Errors

class Stack:
    
    def __init__(self,maxSize):
        self.container =[]
        self.maxSize = maxSize
    
    # isEmpty
    def isEmpty(self):
        return len(self.container)==0
    # isFull
    def isFull(self):
        # check if len(container)>=maxSize 
        return len(self.container)>=self.maxSize
            
    # push
    def push(self,data):
        # check if container is full
        if self.isFull():
            raise containerOverFlow('container is Full')
        self.container.append(data)
        return
    # pop
    def pop(self):
        # check if container is empty
        if self.isEmpty():
            raise containerUnderFlow('container is empty')
        popped_data = self.container.pop()
        return popped_data
    # peek
    def peek(self):
        # check the top element of the container
        if self.isEmpty():
             raise containerUnderFlow('container is empty')
        return self.container[-1]
    
    def empty_container(self):
        self.container.clear()
        return
    
    # display
    def display(self):
        for data in self.container:
            print(data)
        return



container = Stack(maxSize=5)

container.empty_container()

container.push(1)
container.push(2)
container.push(3)
container.push(4)
container.push(5)
# container.push(6)



# container.display()

# container.pop()
# container.pop()
# container.pop()
# container.pop()
# container.pop()


container_top_element = container.peek()

print(f'container_top_element:{container_top_element}')

container.display()

 
    
    
            