class BufferItem:
    
    def __init__(self, item=None):
        self._data = None
        self._next_item = item
    
    @property
    def next_item(self):
        return self._next_item
    @next_item.setter
    def next_item(self, item):
        self._next_item = item
    
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, item):
        self._data = item

class CircularBuffer:
    
    def __init__(self, size):
        self._size = size
        self._count = 0
        self._head = self._tail = temp = BufferItem()
        for _ in range(size - 1):
            temp = BufferItem(temp)
        self._head.next_item = temp

    def push(self, new_item):
        if self.is_full():
            raise Exception("Buffer is full!")
        self.force_push(new_item)
    
    def force_push(self, new_item):
        self._tail.data = new_item
        self._tail = self._tail.next_item
        if self.is_full():
            self._head = self._head.next_item
        if self._count < self._size:
            self._count += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Buffer is empty!")
        else:
            item = self._head.data
            self._head = self._head.next_item
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
        current_item = self._head
        
        for _ in range(self._size):
            buffer_str += "[" + str(current_item.data) + "]"
            head_pointer_str += "-h-" if current_item == self._head else "---"
            tail_pointer_str += "-t-" if current_item == self._tail else "---"
            current_item = current_item.next_item
        
        return ("Buffer:\n" + head_pointer_str + "\n" + buffer_str + "\n" + tail_pointer_str)
