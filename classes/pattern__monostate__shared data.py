"""Monostate idea: to have general state for some piece of data, shared with all existing objects.
If the state changed in one place it is changed at all objects at the same time"""


class ThreadData:
    __shared_attrs = {
        "name": "thread",
        "data": {},
        "id": 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs  # all the local data of all created objects here will be shared between each object

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def get_items(self):
        return self.__shared_attrs

    def set_items(self, key, value):
        self.__shared_attrs[key] = value


thread_1 = ThreadData()
thread_2 = ThreadData()

print(thread_1.__getattribute__('name'))  # returns value of the specified key

thread_2.set_items('id', 18)  # set id to another value

print(thread_2.get_items())  # {'name': 'thread', 'data': {}, 'id': 18}
print(thread_1.get_items())  # {'name': 'thread', 'data': {}, 'id': 18}

thread_1.new_field = "New field has been set"

print(thread_1.__getattribute__("new_field")) # New field has been set
print(thread_2.__getattribute__("new_field")) # New field has been set

