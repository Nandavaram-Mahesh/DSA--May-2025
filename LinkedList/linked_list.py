# First create a node --> Node = {data:value,pointer:None}
class Node:
    def __init__(self,value):
        self.data = value
        self.next_pointer = None

# Now create a linked list
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        # new_node = Node(value)
        # self.head = new_node
        # self.tail = new_node
        # self.length = 1
 
    # function to append a node to the end of the Linkedlist
    def append_node(self,value):
        # create a new node 
        new_node = Node(value)
        # check if the linked list is empty or not
        if self.head is None:
            # if head is empty then make the new node as head and tail
            self.head = new_node
            self.tail = new_node
        # else point the tail nextptr to the new node and then make the new node as tail
        else:
            self.tail.next_pointer = new_node
            self.tail = new_node
        self.length+=1
        # Exit from the fn
        return True
    
    # function to  prepend a node to the Beginning of the Linkedlist
    def prepend_node(self,value):
        # create a new node
        new_node = Node(value)  
        # Edge Case 1
        # check if the linked list is empty
        if self.head is None:
            # If self.head is None then self.head = new_node , self.tail = new_node
            self.head = new_node
            self.tail = new_node
            
        # else new_node.next_ptr = head , head = new_node
        else:
            new_node.next_pointer = self.head
            self.head = new_node
        self.length+=1
        
        # Exit the code
        return True
    
    # function to pop the last node
    def pop_last(self):
        # Edge Case 1
        # if linked list is empty
        if self.head is None:
            return None
        # assign temp and prev pointers to head
        temp = self.head
        prev = self.head
        # Run a loop till temp.next_ptr is not none
        while(temp.next_pointer is not None):
            # assign prev = temp
            prev = temp
            # temp = temp.next_ptr
            temp = temp.next_pointer 
        # when temp.next_ptr is none , we come out of loop
        # assign tail = prev
        self.tail=prev
        # tail.next_ptr = None
        self.tail.next_pointer = None
        # decrement the length 
        self.length-=1
        
        # Edge Case 2  - when there is only one node in the linked list
        if self.length==0:
        # self.head = None
            self.head = None
        # self.tail = None
            self.tail = None
            
    # return temp
        return temp 
     
        #   
    
    # function to pop the first node
    def pop_first(self):
        
        temp = self.head
    # Edge Case 1
        # if linked list is empty
        if self.head is None:
            return None
    # ''' Edge Case 2
    #     # if there is only one node in the linked list
    #     # if self.head.next_pointer is None:
    #     #     self.head = None
    #     #     self.tail = None
    #     #     self.length = 0
    # '''
        # else self.head = self.head.next_pointer        
        else:
            self.head = self.head.next_pointer
            temp.next_pointer = None
        self.length-=1
    # Edge Case 2
        # if there is only one node in the linked list
        if self.length==0:
            self.tail = None
        
        # Exit from the function
        return temp 
    
    def print_list(self):
        print(f"length of linked list: {self.length}")
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next_pointer
        
linked_list_1 = LinkedList()
linked_list_1.append_node(1)
linked_list_1.append_node(2)
linked_list_1.append_node(3)
linked_list_1.append_node(4)
linked_list_1.append_node(5)


linked_list_1.print_list()

# linked_list_1.pop_last()
# linked_list_1.pop_last()
# linked_list_1.pop_last()
# linked_list_1.pop_last()
# linked_list_1.pop_last()
linked_list_1.print_list()


linked_list_1.pop_first()
linked_list_1.pop_first()
linked_list_1.pop_first()
linked_list_1.pop_first()
linked_list_1.pop_first()
linked_list_1.pop_first()
linked_list_1.print_list()