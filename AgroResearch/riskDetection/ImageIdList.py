class idList(list):
    def __setitem__(self, id,value):
        if id >= len(self):
            self.extend([None] * (id + 1 - len(self)))
        list.__setitem__(self, id,value)

