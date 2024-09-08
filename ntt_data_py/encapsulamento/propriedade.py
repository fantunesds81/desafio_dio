class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def X(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def X(self):
        self._x = -1
    


foo = Foo(10)
print(foo.X)

foo.X = 10
print(foo.x)