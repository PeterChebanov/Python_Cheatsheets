"""Global"""

N = 100


def print_N():  # takes local scope of N
    N = 50
    print(f"This is local N: {N}")


def print_global_N():  # takes global scope of N
    global N
    print(f"This is global N: {N}")


print_N()
print_global_N()
print('=' * 50)

"""Nonlocal"""

x = 0


def outer():
    x = 1

    def inner():
        x = 2
        print("inner: ", x)

    inner()
    print("outer: ", x)


outer()  # inner: 2 #outer: 1
print("global:", x)  # global: 0

print('=' * 50)


def non_local_outer():
    x = 1

    def inner():
        nonlocal x  # x will be taken from the upper scope of the func (non_local_outer). if you change it in def inner
        x = 2  # it will be changed in def non_local_outer also
        print(f"inner: {x}")

    inner()
    print(f"outer: {x}")


non_local_outer()  # inner: 2 #outer: 2
print("global:", x)  # global: 0
print('=' * 50)

"""Clojures"""


def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start

    return step


c1 = counter(10)
c2 = counter()

print(c1(), c2())  # 11 1
print(c1(), c2())  # 12 2
print(c1(), c2())  # 13 3
print(c1(), c2())  # 14 4
print('=' * 50)


def strip_string(strip_chars=" "):  # by default strip string by spaces
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


strip_1 = strip_string()
strip_2 = strip_string(" !&^%?.,")

print(strip_1("    Hello Python!!!!   "))
print(strip_2(" hello python?..,  !!"))
print('=' * 50)

"""Decorators"""


def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("Doing something before func will be called")
        res = func(*args, **kwargs)
        print("Doing something after func will finish it's work")
        return res

    return wrapper


def some_func(title, tag):
    print(f"title = {title}, tag = {tag} ")
    return f"<{tag}>{title}</{tag}>"


some_func = func_decorator(some_func)
html_tag = some_func("I love Python", "h1")
print(html_tag)
print('=' * 50)


@func_decorator  # the same as line 111
def some_func_with_python_decoratror(title, tag):
    print(f"title = {title}, tag = {tag} ")
    return f"<{tag}>{title}</{tag}>"


"""parametrized decorator"""


def param_decorator(parameter_x=150):
    def decor_func(func):
        def wrapper():
            print("Actions before calling func with decorator parameter")
            res = func(parameter_x)
            print("Actions after calling func with decorator parameter")
            return res

        wrapper.__name__ = func.__name__  # save the name of the function which is passed as argument but not the wrapper name -> best practice to do so -> the same is done with from functools import wrpas
        wrapper.__doc__ = func.__doc__  # save the doc of the function which is passed as argument but not the wrapper doc  -> best practice to do so -> the same is done with from functools import wrpas
        return wrapper

    return decor_func


@param_decorator(parameter_x=500)
def print_x(parameter_x):
    """Function which prints passed parameter"""
    print(parameter_x)


print_x()
print(print_x.__name__)
print(print_x.__doc__)
print('=' * 50)

from functools import wraps


def param_decorator_with_wrap(parameter_x=150):
    def decor_func(func):
        @wraps(func)  # the same is on lines 134 and 135
        def wrapper():
            print("Actions before calling func with decorator parameter")
            res = func(parameter_x)
            print("Actions after calling func with decorator parameter")
            return res

        return wrapper
    return decor_func

