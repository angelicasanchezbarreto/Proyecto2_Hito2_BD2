import heapq
from typing import List

class MaxHeap:
    def __init__(self):
        self.data = []

    def push(self,val):
        heapq.heappush(self.data,val)

    def pop(self):
        return heapq.heappop(self.data)
    
    def size(self):
        return len(self.data)
    
    def get_k_elem(self,k):
        return self.data[0:k]