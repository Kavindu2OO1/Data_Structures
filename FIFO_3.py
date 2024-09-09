class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class FIFOQueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

    def is_empty(self):
        return self.front is None

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

# Example usage:
queue_linked_list = FIFOQueueLinkedList()
queue_linked_list.enqueue(1)
queue_linked_list.enqueue(2)
print(queue_linked_list.dequeue())  # Output: 1
