# Singly Linked List Node Definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 1. Implement a Stack using Linked List
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            return None
        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        return self.top.data if self.top else None

# 2. Reverse a Linked List
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# 3. Detect a Cycle in Linked List

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# 4. Find the Middle Node
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# 5. Remove N-th Node from End
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    slow = fast = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next

# 6. Merge Two Sorted Linked Lists
def merge_sorted_lists(l1, l2):
    dummy = tail = Node(0)
    while l1 and l2:
        if l1.data < l2.data:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next

# 7. Check Palindrome

def is_palindrome(head):
    vals = []
    while head:
        vals.append(head.data)
        head = head.next
    return vals == vals[::-1]

# 8. Detect and Remove Cycle
def detect_and_remove_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return
    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next
    fast.next = None

# 9. Find Starting Node of Cycle
def find_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

# 10. Reverse Sublist Between m and n
def reverse_between(head, m, n):
    if not head:
        return None
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    for _ in range(m - 1):
        prev = prev.next
    curr = prev.next
    for _ in range(n - m):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp
    return dummy.next
