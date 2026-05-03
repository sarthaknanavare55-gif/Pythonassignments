class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def safe_pop(self):
        if len(self.stack) == 0:
            print("Stack is empty, nothing to pop.")
            return None
        return self.stack.pop()

    def display(self):
        print("Stack:", self.stack)


s = Stack()
s.push(10)
s.push(20)
s.display()

print("Popped:", s.safe_pop())
print("Popped:", s.safe_pop())
print("Popped:", s.safe_pop())