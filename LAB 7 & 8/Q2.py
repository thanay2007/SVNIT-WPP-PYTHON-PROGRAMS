class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        temp = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return temp.data

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" <- ")
            temp = temp.next
        print("None")

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
print("Dequeued:", q.dequeue())
q.display()
