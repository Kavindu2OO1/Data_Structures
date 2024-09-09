class FIFOQueueList:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage:
queue_list = FIFOQueueList()
queue_list.enqueue(1)
queue_list.enqueue(2)
print(queue_list.dequeue())  # Output: 1
