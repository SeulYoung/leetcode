from collections import deque


class Solution:
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()

        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
