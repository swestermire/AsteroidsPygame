class Example:
    def __init__(self):
        self._vals = [1]

    def __getitem__(self, val):
        return self._vals

    def __setitem__(self, idx, val):
        self._vals[idx] = val

    def __str__(self):
        return 'This is your example object'

obj = Example()
print(obj)
print(obj[0], obj[1], obj[2])
obj[0]= 0
print(obj[0], obj[1], obj[2])
