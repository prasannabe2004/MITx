class Queue(object):
    """An intSet is a queue of integers
       FIFO"""

    def __init__(self):
        """Create an empty queue"""
        self.elements = []

    def insert(self, e):
        """ Push e """
        if not e in self.elements:
            self.elements.append(e)

    def remove(self):
        """Pop an element"""
        try:
            return self.elements.pop(0)
        except:
            raise ValueError('ValueError')

    def __str__(self):
        """Returns a string representation of self"""
        return '{' + ','.join([str(e) for e in self.elements]) + '}'

q1 = Queue()
q2 = Queue()
q1.insert(17)
q2.insert(20)
print q1.remove()
print q2.remove()
print q2.remove()

print q1
print q2