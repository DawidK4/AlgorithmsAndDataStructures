class PriorityQueue:
    def __init__(self):
        self.heap = [None]  # Using a list with index 0 unused for easier calculations

    def insert(self, element, priority):
        """Insert an element with the given priority. (O(log n))"""
        self.heap.append((priority, element))
        self._upheap(len(self.heap) - 1)

    def find_min(self):
        """Return the element with the highest priority (lowest number). (O(1))"""
        return self.heap[1][1] if len(self.heap) > 1 else None

    def del_min(self):
        """Remove and return the element with the highest priority. (O(log n))"""
        if len(self.heap) > 1:
            min_element = self.heap[1][1]
            self.heap[1] = self.heap[-1]
            self.heap.pop()
            self._downheap(1)
            return min_element
        return None

    def _upheap(self, index):
        """Restore heap order by moving element up. (O(log n))"""
        while index > 1:
            parent = index // 2
            if self.heap[parent][0] > self.heap[index][0]:  # Compare priorities
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                break

    def _downheap(self, index):
        """Restore heap order by moving element down. (O(log n))"""
        while 2 * index < len(self.heap):
            left_child = 2 * index
            right_child = left_child + 1
            smallest = left_child

            if right_child < len(self.heap) and self.heap[right_child][0] < self.heap[left_child][0]:
                smallest = right_child

            if self.heap[index][0] > self.heap[smallest][0]:  # Swap if parent is greater
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def construct(self, elements):
        """Efficiently build the heap from a list of (element, priority) tuples. (O(n))"""
        self.heap = [None] + elements  # Initialize heap, keep index 0 unused
        for i in range(len(self.heap) // 2, 0, -1):
            self._downheap(i)

    def is_empty(self):
        """Check if the priority queue is empty. (O(1))"""
        return len(self.heap) == 1