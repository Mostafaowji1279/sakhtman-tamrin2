class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class List:
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head
        self.n = 0

    def get(self, ind):
        if ind >= self.size():
            raise Exception('Out of list')
        x = self.head.next
        for _ in range(ind):
            x = x.next
        return x

    def insert_after(self, x, data):
        y = Node(data)
        self.n += 1
        y.prev = x
        y.next = x.next
        x.next = y
        y.next.prev = y
        return y

    def delete(self, x):
        if self.size() == 0:
            raise Exception('List is empty')
        self.n -= 1
        x.prev.next = x.next
        x.next.prev = x.prev
        return x

    def find(self, val):
        x = self.head.next
        for _ in range(self.size()):
            if x.data == val:
                return x
            x = x.next
        return None

    def size(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    def print_list_values(self):
        values = []
        x = self.head.next
        for _ in range(self.size()):
            values.append(x.data)
            x = x.next
        print(values)