'''
可動態添加屬性和方法
@staticmethod?
@classmethod?

__slots__: define allowed properties

'''

import types


class Person(object):
    __slots__ = ('name', 'location', 'gender')

    def __init__(self, newName):
        self.name = newName

    def entertaining(self):
        print('dancing,...')


# add properties to class
Person.location = 'China'


# add properties to instance
anna = Person('anna')
anna.gender = 'female'


def work(self):
    print('....{} is working'.format(self.name))


# add methods to instance
anna.work = types.MethodType(work, anna)
anna.work()

# below works the same, but above way is more explicity
work = types.MethodType(work, anna)
work()

# add static method to class
@staticmethod
def static_method():
    print('....static_method.....')


anna.static_method = static_method
anna.static_method()


@classmethod
def add_class_method(kls):
    print('....add class method..')


Person.add_class_method = add_class_method
Person.add_class_method()

