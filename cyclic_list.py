class cyclic_list:

    def __init__(self, length):
        self.container = []
        self.maxlength = length
        self.length = 0
        self.pos = 0

    def __repr__(self):
        return repr(self.container[self.pos])

    def add(self, object):
        if self.length == self.maxlength:
            raise Exception("Maximum capacity exceeded.")
            return
        self.length += 1
        self.container.append(object)

    def get_current(self):
        if self.length == 0:
            raise Exception("Container is empty!")
            return
        return self.container[self.pos]

    def get_next(self):
        if self.length == 0:
            raise Exception("Container is empty!")
            return
        if self.pos == self.maxlength - 1 or self.pos > self.length -1:
            self.pos = 0
            return self.container[self.pos]
        self.pos += 1
        return self.container[self.pos]

    def get_skip(self, n):
        if self.length == 0:
            raise Exception("Container is empty!")
            return
        self.pos += n
        if self.pos > self.length - 1:
            self.pos -= self.length - 1
        if self.pos > self.maxlength:
            self.pos -= self.maxlength
        return self.container[self.pos]