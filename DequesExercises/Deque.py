# Double ended queue
# We can add items at the beginning or at the end of the deque
class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # Like Stack
    def addFront(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop()

    # Like Queue
    def addRear(self, item):
        self.items.insert(0, item)

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        print(len(self.items))

def testing_deque():

    deque = Deque()

    print(deque.isEmpty())

    deque.addFront('hello')

    deque.addRear('juliana')

    deque.size()

    print("Removing front and rear element: " + deque.removeFront() + ' ' + deque.removeRear())

    deque.size()

    print(deque.isEmpty())

