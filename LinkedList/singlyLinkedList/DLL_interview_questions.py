# Singly Linked List Node Definition
class Node:
    def __init__(self, data):
        print(f"Creating node with data: {data}")
        self.data = data
        self.next = None

# Doubly Linked List Node Definition
class DNode:
    def __init__(self, data):
        print(f"Creating doubly linked list node with data: {data}")
        self.data = data
        self.prev = None
        self.next = None

# 1. Insert at Head
def insert_at_head(head, data):
    node = DNode(data)
    node.next = head
    if head:
        head.prev = node
    return node

# 2. Insert at Tail
def insert_at_tail(head, data):
    node = DNode(data)
    if not head:
        return node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = node
    node.prev = curr
    return head

# 3. Delete Node by Value
def delete_node(head, value):
    curr = head
    while curr and curr.data != value:
        curr = curr.next
    if not curr:
        return head
    if curr.prev:
        curr.prev.next = curr.next
    else:
        head = curr.next
    if curr.next:
        curr.next.prev = curr.prev
    return head

# 4. Traverse Forward and Backward
def traverse_dll(head):
    forward = []
    curr = head
    last = None
    while curr:
        forward.append(curr.data)
        last = curr
        curr = curr.next
    backward = []
    while last:
        backward.append(last.data)
        last = last.prev
    return forward, backward

# 5. Find Length
def get_length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

# 6. Reverse DLL
def reverse_dll(head):
    curr = head
    temp = None
    while curr:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        curr = curr.prev
    return temp.prev if temp else None

# 7. Remove Duplicates from Sorted DLL
def remove_duplicates_dll(head):
    curr = head
    while curr and curr.next:
        if curr.data == curr.next.data:
            nxt = curr.next
            curr.next = nxt.next
            if nxt.next:
                nxt.next.prev = curr
        else:
            curr = curr.next
    return head

# 8. Check Palindrome
def is_dll_palindrome(head):
    if not head:
        return True
    left = head
    right = head
    while right.next:
        right = right.next
    while left != right and left.prev != right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev
    return True

# 9. Insert After a Node
def insert_after_node(node, data):
    new_node = DNode(data)
    new_node.next = node.next
    new_node.prev = node
    if node.next:
        node.next.prev = new_node
    node.next = new_node

# 10. Insert Before a Node
def insert_before_node(node, data):
    new_node = DNode(data)
    new_node.prev = node.prev
    new_node.next = node
    if node.prev:
        node.prev.next = new_node
    node.prev = new_node
    return new_node if not new_node.prev else None

# 11. Find Pairs with Target Sum
def find_pairs_with_sum(head, target):
    pairs = []
    left = head
    right = head
    while right.next:
        right = right.next
    while left != right and right.next != left:
        total = left.data + right.data
        if total == target:
            pairs.append((left.data, right.data))
            left = left.next
            right = right.prev
        elif total < target:
            left = left.next
        else:
            right = right.prev
    return pairs

# 12. Flatten Multilevel DLL
class MultiLevelNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.child = None

def flatten_multilevel_dll(head):
    if not head:
        return head
    stack = []
    curr = head
    while curr:
        if curr.child:
            if curr.next:
                stack.append(curr.next)
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
        if not curr.next and stack:
            curr.next = stack.pop()
            curr.next.prev = curr
        curr = curr.next
    return head

# 13. Clone DLL with Random Pointer
class RandomDNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        self.random = None

def clone_dll_with_random(head):
    if not head:
        return None
    curr = head
    while curr:
        new_node = RandomDNode(curr.val)
        new_node.next = curr.next
        curr.next = new_node
        new_node.prev = curr
        curr = new_node.next
    curr = head
    while curr:
        if curr.next:
            curr.next.random = curr.random.next if curr.random else None
        curr = curr.next.next
    dummy = RandomDNode(0)
    copy = dummy
    curr = head
    while curr:
        copy.next = curr.next
        curr.next = curr.next.next
        copy = copy.next
        curr = curr.next
    return dummy.next

# 14. Rotate DLL by K

def rotate_dll(head, k):
    if not head or k == 0:
        return head
    length = get_length(head)
    k %= length
    if k == 0:
        return head
    curr = head
    for _ in range(length - k - 1):
        curr = curr.next
    new_head = curr.next
    new_head.prev = None
    curr.next = None
    tail = new_head
    while tail.next:
        tail = tail.next
    tail.next = head
    head.prev = tail
    return new_head

# 15. Convert Binary Tree to DLL (In-order)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_to_dll(root):
    def in_order(node):
        nonlocal prev, head
        if not node:
            return
        in_order(node.left)
        dll_node = DNode(node.val)
        if prev:
            prev.next = dll_node
            dll_node.prev = prev
        else:
            head = dll_node
        prev = dll_node
        in_order(node.right)
    prev = head = None
    in_order(root)
    return head
