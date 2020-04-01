from functools import partial
import inspect
# def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         value = next(it)
#     else:
#         value = initializer
#     for element in it:
#         value = function(value, element)
#     return value

# print(reduce(lambda value,x:value + x, range(5),10))
def add(x,y):
    return x + y

newadd = partial(add,x=4,y=5)
print(inspect.signature(newadd))  #
print(newadd(x=10,y=11))   #==>21
print(inspect.signature(newadd))


