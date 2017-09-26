from linkedlist import LinkedList

"""            Array           LinkedList
Space          O(n)              O(n)
Enqueue        O(1)              O(1)
Dequeue        O(1)              O(1)   
Size           O(1)              O(1)   
"""

class ArrayQueue(object):

    def __init__(self, capacity):
        self.items = [0]*capacity
        self.head = None
        self.tail = None
        self.size = 0
        self.capacity = capacity

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return (self.tail+1) % self.capacity == self.head
        return self.size == self.capacity
    
    def size():
        return (self.capacity - self.tail + self.head + 1) % self.capacity

    def enqueue(self, data):
        # Full list of capacity
        if self.isFull():
            return  "Overflow"
        # Empty list
        if self.head is None and self.tail is None:
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.capacity
        self.items[self.tail] = data
        self.size += 1

    def dequeue(self):
        # Empty list
        if self.isEmpty():
            return "Underflow"
        if self.head is None and self.tail is None:
            return None
        data = self.items[self.head]
        # Remove only element from a one element list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return data




# List Queue
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class ListQueue(object):

    def __init__(self, capacity=0):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def enqueue(self, data):
        # Full list of capacity
        if self.isFull():
            return  "Overflow"
        node = Node(data)
        # Empty list
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        # Empty list
        if self.isEmpty():
            return "Underflow"
        if self.head is None and self.tail is None:
            return None
        data = self.head.data
        self.size -= 1
        # Remove only element from a one element list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return data

class DeQueue(object):
    def __init__(self, head=None, tail = None):
        self.head = head
        self.tail = tail

    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def __repr__(self):
        s = ''
        curr = self.head
        while curr is not None:
            s = s + str(curr) + " -> "
        s += "None"
        return s

    def insert_at_head(self, data):
        if data is None:
            return None
        node = DeNode(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        return node

    def insert_at_tail(self, data):
        if data is None:
            return None
        node = DeNode(data)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        return node

    def delete_at_head(self):
        if self.head is None:
            return None
        head_node = self.head
        node = self.head.next
        if node is not None:
            node.prev = None
        else:
            self.tail = None
        self.head = node
        return head_node

    def delete_at_tail(self, data):
        if self.tail if None:
            return None
        tail_node = self.tail
        prev_node = self.tail.prev
        if prev_node is not None:
            prev_node.next = None
        else:
            self.head = None

        self.tail = prev_node
        return tail_node
