# LIFO
class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        # You are appending because it is a LIFO
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        print(self.items[len(self.items)-1])

    def size(self):
       len(self.items)

def testing_stack():

    stack = Stack()

    print(stack.isEmpty())

    stack.push(1)

    stack.push('two')

    stack.peek()

    stack.size()

    stack.pop()

    stack.peek()

    stack.size()

