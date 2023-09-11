class Stack:
    def __init__(self, limit=None):
        self.items = []
        self.limit = limit  # Optional limit for the Stack

    def push(self, value):
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(value)
        else:
            raise ValueError("Stack is full")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def empty(self):
        return self.is_empty()

    def full(self):
        if self.limit is not None:
            return len(self.items) >= self.limit
        return False

    def search(self, value):
        if value in self.items:
            return len(self.items) - self.items.index(value) - 1
        return -1
