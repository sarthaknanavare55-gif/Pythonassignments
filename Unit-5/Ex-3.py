from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty, cannot dequeue.")
            return None
        return self.queue.popleft()

    def display(self):
        print("Queue:", list(self.queue))


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.display()

print("Dequeued:", q.safe_dequeue())
print("Dequeued:", q.safe_dequeue())
print("Dequeued:", q.safe_dequeue())