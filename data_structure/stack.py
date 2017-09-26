from linkedlist import LinkedList

"""            Array           LinkedList
Space          O(n)              O(n)
Push           O(1)              O(1)
Pop            O(1)              O(1)   
Size           O(1)              O(1)   
Top            O(1)              O(1)   
Pop            O(1)              O(1)   
"""


# Need to implement Stack using Queue and Single Array

# Array Implementation of Stack
class ArrayStack(object):
    def __init__(self, capacity):
        self.items = [None]*capacity
        self.top = capacity
        self.capacity = capacity

    def __repr__(self):
        s = ""
        size = len(self)
        while size:
            if s is "":
                s = str(self.items[size-1])
            else:
                s = s+"->"+str(self.items[size-1])
            size -= 1
        return s

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0
    
    def isFull(self):
        return len(self.items) == self.capacity

    def push(self, item):
        if self.isFull(): 
            return "Overflow"
        if self.top is not None:
            self.top = self.top + 1
        else:
            self.top = 0
        self.size += 1
        self.items[self.top] = item

    def pop(self):
        if self.isEmpty(): 
            return "Underflow"
        item = self.items[self.top]
        self.items[self.top] = 0 
        if self.top == 0:
            self.top = None
        else:
            self.top = self.top - 1
        return item
    
    def top(self):
        if self.isEmpty(): 
            return None
        return self.items[self.top]
    
    def size(self):
        if self.top is not None
            return self.top + 1
        return 0



# Linked List implementation of Stack
class ListStack(object):
    def __init__(self, capacity, iterable):
        self.top = LinkedList()
        self.capacity = capacity
        self.size = 0

    def __len__(self):
        return len(self.top)

    def __repr__(self):
        return repr(self.top)

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def push(self, data):
        if self.size < self.capacity:
            self.size += 1
            return self.top.insert_at_head(data)
        else:
            return "Overflow occurs !!!"

    def pop(self):
        if self.size == 0:
            return "UnderFlow occurs !!!"
        node = self.top.head
        self.top.head = self.top.head.next
        return node

    def top(self):
        if self.size == 0: 
            return None
        return self.top.head

