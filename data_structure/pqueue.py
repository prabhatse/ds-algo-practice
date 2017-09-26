from heap import *


class PriorityQueueNode(object):

    def __init__(self, obj, key):
        self.obj = obj
        self.key = key

    def __repr__(self):
        return str(self.obj) + ': ' + str(self.key)


class PriorityQueue(object):

    def __init__(self, capacity):
        self.queue = MinHeap(capacity)

    def insert(self, node):
        self.queue.insert_key(data)

    def extract_min(self):
    	return self.queue.extract_min()

        if not self.queue:
            return None
        minimum = sys.maxsize
        for index, node in enumerate(self.queue):
            if node.key < minimum:
                minimum = node.key
                minimum_index = index
        node = self.queue.pop(minimum_index)
        return node.obj
