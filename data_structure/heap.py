from __future__ import division

import sys

"""            Array           LinkedList
Space          O(n)              O(n)
Get Min/Max    O(1)              O(1)
Dequeue        O(1)              O(1)   
Size           O(1)              O(1)   
"""


class MinHeap(object):

    def __init__(self, capacity):
        self.array = [float('inf')]*capacity
        self.capacity = capacity
        self.heap_size = 0

    def __len__(self):
        return len(self.array)

    def swap(self, l, r):
        self.array[l], self.array[r] = self.array[r], self.array[l]
    
    def left_child(self, index):
        return (2*index + 1)

    def right_child(self, index):
        return (2*index + 2)

    def parent(self, index):
        return (index -1) // 2
    
    def min_heapify(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < self.heap_size and self.array[left] < self.array[index]:
            smallest = left

        if right < self.heap_size and self.array[right] < self.array[smallest]:
            smallest = right

        if smallest != index:
            # Swapping smallest and index values
            self.swap(smallest, index)
            self.min_heapify(smallest)

    def get_mini(self):
        if self.heap_size:
            return self.array[0]
        return None

    def extract_min(self):
        if not self.heap_size:
            return None
        if len(self.array) == 1:
            self.heap_size -= 1
            return self.array[0]
        minimum = self.array[0]
        # Move the last element to the root
        self.array[0] = self.array[self.heap_size - 1]
        self.heap_size -= 1
        self.min_heapify(index=0)
        return minimum

    def decrease_key(self, index, key):
        self.array[index] = key
        self._bubble_up(index)

    def insert_key(self, key):
        if key is None:
            return TypeError('key cannot be None')
        self.array[self.heap_size] = value
        self.heap_size += 1
        self._bubble_up(self.heap_size - 1)

    def delete_key(self, index):
        self.decrease_key(index, -1*float('inf'))
        self.extract_min()

    def peek_min(self):
        return self.array[0] if self.array else None

    def _bubble_up(self, index):
        if index == 0:
            return
        index_parent = self.parent(index)
        if self.array[index] < self.array[index_parent]:
            # Swap the indices and recurse
            self.swap(index, index_parent)
            self._bubble_up(index_parent)


class MaxHeap(object):

    def __init__(self, capacity):
        self.array = [-1*float('inf')]*capacity
        self.capacity = capacity
        self.heap_size = 0

    def __len__(self):
        return len(self.array)

    def swap(self, l, r):
        self.array[l], self.array[r] = self.array[r], self.array[l]
    
    def left_child(self, index):
        return (2*index + 1)

    def right_child(self, index):
        return (2*index + 2)

    def parent(self, index):
        return (index -1) // 2
    
    def max_heapify(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < self.heap_size and self.array[left] > self.array[index]:
            largest = left

        if right < self.heap_size and self.array[right] > self.array[largest]:
            largest = right

        if largest != index:
            # Swapping smallest and index values
            self.swap(largest, index)
            self.max_heapify(largest)

    def get_max(self):
        if self.heap_size:
            return self.array[0]
        return None

    def extract_max(self):
        if not self.heap_size:
            return None
        if len(self.array) == 1:
            self.heap_size -= 1
            return self.array[0]
        minimum = self.array[0]
        # Move the last element to the root
        self.array[0] = self.array[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heapify(index=0)
        return minimum

    def decrease_key(self,index , key):
        self.array[index] = key
        self._bubble_up(index)

    def insert_key(self, key):
        if key is None:
            return TypeError('key cannot be None')
        self.array[self.heap_size] = value
        self.heap_size += 1
        self._bubble_up(self.heap_size - 1)

    def delete_key(self, index):
        self.decrease_key(index, 1*float('inf'))
        self.extract_max()

    def peek_min(self):
        return self.array[0] if self.array else None

    def _bubble_up(self, index):
        if index == 0:
            return
        index_parent = self.parent(index)
        if self.array[index] > self.array[index_parent]:
            # Swap the indices and recurse
            self.swap(index, index_parent)
            self._bubble_up(index_parent)

    def _build_max_heap(self):
        if not self.heap_size:
            return None
        start = (self.heap_size -2) // 2 
        for i in range(start, -1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        self._build_max_heap()
        while self.heap_size > 1:
            self.swap(0, self.heap_size - 1)
            self.heap_size -= 1
            self.max_heapify(0)
        return self.array
