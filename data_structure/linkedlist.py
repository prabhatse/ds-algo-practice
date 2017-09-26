# Implementation of linked linked lists, SLL, DLL, CLL

class Node(object):

	def __init__(self, data):
		self.next = next
		self.data = data

	def __str__(self):
		return self.data

class DeNode(object):
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

# There are three use cases for insertion and deletion of linked list
"""
  at head, at tail, in middle
"""

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

    def __len__(self):
    	current = self.head
        count = 0`
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

    def get_all_data(self):
        data = []
        curr_node = self.head
        while curr_node is not None:
            data.append(curr_node.data)
            curr_node = curr_node.next
        return data

	def insert_at_head(self, data):
		if data is None:
			return None
		node = Node(data)
		node.next = self.head
		self.head = node

	def insert_in_sorted(self, data):
		if data is None:
			return None

		node = Node(data)

        if self.head is None:
        	self.head = node
		    return node

		curr = self.head
		prev = curr
		while curr is not None and curr.data < data:
			prev = curr
			curr = curr.next
		if not prev:
			node.next = self.head
			self.head  = node
        else:
        	if not curr:
        		prev.next = node
        	else:
        		node.next = curr
        		prev.next = node
        return node

	def append(self, data):
		if data is None:
			return None
		node = Node(data)
		if self.head is None:
			self.head  = node
			return node
		curr = self.head
		while curr.next is not None:
			curr = curr.next
        curr.next = node
        return node

    def find_node(self, data):
    	if data is None or self.head is Node:
    		return None
    	curr = self.head
    	while curr is not None and curr.data != data:
    		curr = curr.next
    	return curr


    def delete_node(self, data):
    	if data is None:
    		return None
        if self.head.data == data:
        	node = self.head
        	self.head = node.next
            del node
            return

    	curr = self.head

    	while curr.next is not None:
    		if curr.next.data == data:
    			node = curr.next
    			curr.next = curr.next.next
    			del node
    			return
        return


    def delete_list(self):
    	curr = self.head
    	while curr is not None:
    		curr_next = curr.next
    		del curr
    		curr = curr_next
    	self.head = None

    def count_nodes(self):
    	current = self.head
        count = 0
    	while current is not None:
    		count += 1
    		current = current.next
    	return count

class DoublyLinkedList(object):
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

	def append(self, data):
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

    def insert_in_sorted(self, data):
		if data is None:
			return None

        if self.tail is None or self.head is None or (self.head is not None and data <= self.head.data):
        	return self.insert_at_head(data)
        if data >= self.tail.data:
        	return self.append(data)

        curr = self.head
        while curr.next is not None and curr.next.data < data:
        	curr = curr.next

        node = DeNode(data)
        node.next = curr.next
        curr.next.prev = node
        node.prev = curr
        return node

    def delete(self, data):
    	if data is None or self.head is None:
    		return None


    	if self.head.data == data:
    		node = self.head.next
    		if node is not None:
    			node.prev = None
    		else:
    			self.tail = None
    		self.head = node
    		return

        if self.tail.data == data:
        	self.tail = self.tail.prev
        	self.tail.next = None
        	return None

        curr = self.head
        while curr.next is not None and curr.next.data != data:
        	curr = curr.next
        if curr.next is None:
        	return

        curr.next = curr.next.next
        curr.next.prev = curr
        return


class CircularLinkedList(object):
	def __init__(self, head=None):
		self.head = head

    def __len__(self):
    	current = self.head
        count = 0`
    	while current is not None and curr != self.head:
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
		node = Node(data)
		if self.head is None:
			self.head = node
			node.next = self.head
			return node

		curr = self.head
        while curr.next != self.head:
        	curr = curr.next
        node.next = self.head
        self.head = node
        curr.next = self.head
        return node

	def append(self, data):
		if data is None:
			return None
		node = Node(data)
		if self.head is None:
			self.head = node
			node.next = self.head
			return node

		curr = self.head
        while curr.next != self.head:
        	curr = curr.next
        curr.next = node
        node.next = self.head
        return node

	def insert_in_sorted(self, data):
		if data is None:
			return None
		node = Node(data)
        if self.head is None:
        	self.head = node
        	self.head.next = self.head
		    return node

		curr = self.head
		while curr.next is not None and curr.next.data < data:
			curr = curr.next

		if curr.next is None:
			node.next = self.head
            curr.next = node
        else:
        	node.next = curr.next
        	curr.next = node
        return node

    def delete_node(self, data):
    	if data is None:
    		return None
        if self.head.data == data:
        	node = self.head
        	if self.head != node.next:
        		self.head = node.next
        	else:
        		self.head = None
            del node
            return

    	curr = self.head
    	while curr.next is not None:
    		if curr.next.data == data:
    			node = curr.next
    			curr.next = curr.next.next
    			del node
    			return
        return


    def delete_list(self):
    	curr = self.head
    	while curr is not None:
    		curr_next = curr.next
    		del curr
    		curr = curr_next
    	self.head = None

    def count_nodes(self):
    	current = self.head
        count = 0
    	while current is not None:
    		count += 1
    		current = current.next
    	return count
