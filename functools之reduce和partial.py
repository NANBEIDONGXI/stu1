#这个是紧接着类型注解的讲解

import inspect
from inspect import Parameter
from functools import update_wrapper,wraps

def check(fn):
    def wrapper(*args,**kwargs):
        sig  = inspect.signature(fn)
        params = sig.parameters
        values = list(params.values())
        flag = True
        for i,x in enumerate(args): #这里判断的事位置参数，要是传参用的关键字，这里就进不来，判断不了，所以还需要判断下kwargs
            param:Parameter = values[i]
            if param.annotation != inspect._empty and not isinstance(x,param.annotation):
                print(x,'not ok')
                # flag = False
                # break
            else:
                print(x,'ok')
        for k,v in kwargs.items():
            param:Parameter = params[k]

            if param.annotation != inspect._empty not isinstance(v,param.annotation):
                print(v, 'not ok&&')
            else:
                print(v, 'ok&&&&')
        return fn
    return wrapper

@check   #相当于 add = check(add)，这里确实有函数调用 add=wrapper  这里执行的话，无论下面add函数有没有执行，check函数都会执行。
def add(x:int,y:int=7) -> int:
    return x + y

# check(add)(4,5)  #调用测试，或者用@check装饰器，放在add函数之前
add(4,5)
add(x=14,y=15)
add(4,y=5)

######################################################################################################
from functools import reduce
#下面是reduce的源代码
# def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         value = next(it)
#     else:
#         value = initializer
#     for element in it:
#         value = function(value, element)
#     return value

reduce(lambda value,x:value + x, range(5),10)  # ==》20 这是累加，10是初始值，不给初始值，就从可迭代对象中拿一个，然后累加

##################################################################################################################

functools模块
partial方法   partial：部分的，局部的
    偏函数，把函数部分的参数固定下来，相当于为部分的参数添加了一个固定的默认值，形成一个新的函数并返回
    从partial生成的新函数，是对原函数的封装

#参考文档里面的
# def partial(func, /, *args, **keywords):
#     def newfunc(*fargs, **fkeywords):      #包装函数
#         newkeywords = {**keywords, **fkeywords}
#         # newkeywords.update(fkeywords)    #这句跟上面是一样
#         return func(*args, *fargs, **newkeywords)  #先传入的参数放在前面
#     newfunc.func = func            #保留原函数
#     newfunc.args = args            #保留原函数的位置参数
#     newfunc.keywords = keywords    #保留原函数的关键字参数
#     return newfunc

from functools import partial，update_wrapper,wraps
improt inspect

def add(x,y):
    return x + y

newadd = partial(add,4)  #先传入的参数放在前面
print(inspect.signature(newadd))  #==> (y)，这相当于只传了参数y
print(newadd(5))   #==>9

newadd = partial(add,y=5)
print(inspect.signature(newadd))   #==>(x,*,y=5),这里看着应该只有x传入，但这里的y已经被固定下来了，但是y还是可以被更新的，加个*,显示y为keyword_only
print(newadd(4))   #==>9

newadd = partial(add,x=4,y=5)
print(inspect.signature(newadd))  #==>(*,x=4,y=5),x,y都被固定下来了，再要传参的话只能是keyword_only了，所以返回这个可以理解吧
print(newadd())   #==>9

newadd = partial(add,x=4,y=5)
print(inspect.signature(newadd))  #==>(*, x=4, y=5)
print(newadd(x=10,y=11))   #==>21

# newadd = partial(add,x=4)
# print(newadd(5))    这句不行，这里相当于x 定义了两次，没有传入y



