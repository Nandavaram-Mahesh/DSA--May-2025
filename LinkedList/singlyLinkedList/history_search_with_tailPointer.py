class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class SearchHistory:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length=0
    
    def add_search(self,value):
        # create a new node
        new_node = Node(value)
        # check if LL is empty
        if self.head is None:
            # if empty then make new node as head and tail
            self.head = self.tail = new_node
        # else point the tail nextptr to the new node and then make the new node as tail
        else:
            self.tail.next = new_node
            self.tail = new_node
        # increment the length
        self.length+=1

    def view_history(self):
        # check if LL is empty
        if self.head is None:
            print("History is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next
        return

    def search_query(self,keyword):
         # check if LL is empty
        if self.head is None:
            print("History is empty")
            return
        current = self.head
        found = False
        while current:
            if keyword.lower() in current.data.lower():
                print(f"Found: {current.data}")
                found = True
            current = current.next
    
        
        if not found:
            print(f"No search found containing '{keyword}'.")

    def clear_history(self):
            """Clear all search history."""
            self.head = None
            self.tail = None
            print("Search history cleared.")

# Client Code
history = SearchHistory()

history.add_search("Learn Python")
history.add_search("Graph implementation in Python")
history.add_search("Stack vs Queue")
history.add_search("Dequeue vs Queue implementation")
history.add_search("Enqueue vs Dequeue implementation")
history.add_search("Singly Linked List tutorial")

history.view_history()

print("\nSearch for 'queue':")
history.search_query("queue")

print("\nSearch for 'recursion':")
history.search_query("recursion")

print("\nClearing history...")
history.clear_history()

history.view_history()
