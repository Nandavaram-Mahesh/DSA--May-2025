class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_front(self,value):
        # Create a new_node
        new_node = Node(value)
        # Checking if the LL is empty
        if self.head is None:
            self.head = new_node
            return
        # else point the new node to the head and make the new node as head
        new_node.next = self.head
        self.head = new_node
    
    def delete_at_front(self):
        # check if the LL is empty
        if self.head is None:
            print("Linked list is empty")
            return
        # else make head as next
        temp = self.head 
        self.head = self.head.next
        temp.next = None
        return
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp=temp.next




linked_list = LinkedList()
linked_list.insert_at_front(10)
linked_list.insert_at_front(20)
linked_list.insert_at_front(30)
linked_list.insert_at_front(40)
# linked_list.delete_at_front()
# linked_list.display()


# linked_list.delete_at_front()
linked_list.display()