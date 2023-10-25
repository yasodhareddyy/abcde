class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # Main stack for enqueue
        self.stack2 = []  # Temporary stack for dequeue

    def enqueue(self, item):
        # To enqueue, simply push the item onto stack1
        self.stack1.append(item)

    def dequeue(self):
        # If stack2 is empty, transfer elements from stack1
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Pop from stack2 to perform dequeue
        if self.stack2:
            return self.stack2.pop()
        else:
            return "Queue is empty"

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def size(self):
        return len(self.stack1) + len(self.stack2)

# Example usage
queue = QueueUsingStacks()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Should print 1
print(queue.dequeue())  # Should print 2

queue.enqueue(4)
print(queue.dequeue())  # Should print 3
print(queue.dequeue())  # Should print 4

print(queue.is_empty())  # Should print True



