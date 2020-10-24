class Stack:
    def __init__(self):
        self._data = []


    @property
    def size(self):
        return len(self._data)

    def push(self, element):
        self._data.append(element)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[-1]

    def clear(self):
        self._data.clear()