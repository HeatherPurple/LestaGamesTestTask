class CircularBuffer:
    
    def __init__(self, size):
        self._size = size
        self._items = [None] * size
        self._head = 0
        self._tail = -1
        self._count = 0

    def push(self, new_item):
        if self.is_full():
            raise Exception("Buffer is full!")
        self.force_push(new_item)
    
    def force_push(self, new_item):
        self._tail = (self._tail + 1) % self._size 
        self._items[self._tail] = new_item
        if self.is_full():
            self._head = (self._head + 1) % self._size
        if self._count < self._size:
            self._count += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Buffer is empty!")
        else:
            item = self._items[self._head]
            self._head = (self._head + 1) % self._size
            self._count -= 1
            return item

    def is_empty(self):
        return self._count == 0
    
    def is_full(self):
        return self._count == self._size
    
    def count(self):
        return self._count

    def __str__(self):
        buffer_str = ""
        tail_pointer_str = ""
        head_pointer_str = ""
        
        i = 0
        for item in self._items:
            buffer_str += "[" + str(item) + "]"
            head_pointer_str += "-h-" if i == self._head else "---"
            tail_pointer_str += "-t-" if i == self._tail else "---"
            i += 1
        
        return ("Buffer:\n" + head_pointer_str + "\n" + buffer_str + "\n" + tail_pointer_str)
