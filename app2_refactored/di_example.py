class Object:
    pass

class Example1(Object):
    pass

class Example2(Object):
    pass

class MyClass:
    def __init__(self, object_: Object):
        self.object = object_


my_class = MyClass(object_=Example1())
my_class = MyClass(object_=Example2())
