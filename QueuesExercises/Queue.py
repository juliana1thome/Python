# FIFO
class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        # 0 because FIFO
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        print(len(self.items))

def testing_queue():

    queue = Queue()

    print(queue.isEmpty())

    queue.enqueue(1)

    queue.enqueue('two')

    queue.size()

    queue.dequeue()

    queue.size()

    print(queue.isEmpty())

