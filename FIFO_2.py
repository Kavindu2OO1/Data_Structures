from collections import deque

class FIFOQueueDeque:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage:
queue_deque = FIFOQueueDeque()
queue_deque.enqueue(1)
queue_deque.enqueue(2)
print(queue_deque.dequeue())  # Output: 1
