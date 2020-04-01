functools 模块
from functools import lru_cache
import time
@functools.lru_cache(maxsize = 128, typed = False)
    Least-recently-used装饰器。lru, 最近最少使用。 cache缓存
    如果maxsize设置为None, 则禁用LRU功能， 并且缓存可以无限增长。 当maxsize是2的幂时，LRU功能执行的最好
    如果typed设置为True，则不同类型的函数参数将单独缓存。例如，f(3)和f(3.0)将被视为具有不同结果的不同调用

from functools import lru_cache
import time
@lru_cache()       #带参装饰器
def add(x=4,y=5):
    time.sleep(3)
    return x + y
print(1,add(4,5))
print(2,add(4))
print(3,add(y=5))
print(4,add(x=4,y=5))
print(5,add(y=5,x=4))
#这上面的每一种都不一样，都要缓存，但是再重复执行上面的print语句后，可以很快得出结果，已经有缓存了

lru_cache装饰器
    通过一个字典缓存被装饰函数的调用和返回值
    key是什么？分析代码看看
        functools._make_key((4,6),{'z':3},False)
        functools._make_key((4,6,3),{},False)
        functools._make_key(tuple(),{'z':3,'x':4,'y':6},False)
        functools._make_key(tuple(),{'z':3,'x':4,'y':6},True)

##################################################################################
斐波那契数列改造

@lru_cache()   #加个这，速度就快多了，缓存了
def fib(n):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)

fib(10)
for i in range(11):
    print(fib(i))

###########################################################################
# lru_cache()装饰器应用
#     使用前提
#         同样的函数参数一定得到同样的结果
#         函数执行时间很长，且要多次执行
#     本质是函数调用的参数=》返回值
#     缺点：
#         不支持缓存过期，key无法过期，失效
#         不支持清除操作
#         不支持分布式，是一个单机的缓存
#     使用场景，单机上需要空间换时间的地方，可以用缓存将计算变成快速的查询







