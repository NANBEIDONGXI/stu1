# tail = " ".join([str(i) for i in range(12,0,-1)])
# a = [str(i) for i in range(6)]
# print(tail)
# print(list(tail))
# for i in tail:
#     print(i,end = ' ')
# # print(tail[1])
# print(a)
# b = ' '.join(a)
# print(b)
# print(b[0])
# print(b[1])
# print(b[2])
# def fn(x):
#     for i in range(x):
#         if i > 3:
#             return i
#     else:
#         print('{} is not greater than 3'.format(x))
# fn(2)
# def foo(w,u='abc',*,z=123,zz=[456]):
#     print(w,u,z,zz)
#     u='xyz'
#     z=789
#     zz.append(1)
#     print(w,u,z,zz)
# print(foo.__defaults__)
# print(foo.__kwdefaults__)
# foo('magedu')
# print(foo.__defaults__)
# print(foo.__kwdefaults__)#列表，字典等复杂类型，要注意了
'''
def foo(xyz=[],u='abc',z=123):
    xyz = xyz[:]#影子拷贝，xyz则重新被执行新的内存对象
    xyz.append(1)
    print(xyz)
foo()

foo([10])
print(foo.__defaults__)
foo([10,5])
print(foo.__defaults__)

def foo1(b,b1=3):
    print("foo1 called",b,b1)
def foo2(c):
    foo3(c)
    print("foo2 called",c)
def foo3(d):
    print("foo3 called",d)
def main():
    print("main called")
    foo1(100,101)
    foo2(200)
    print("main ending")
main()

num = [1,2,1,2,-1,0,0]
for n in num:
    if n ==0:
        num.remove(n)
print('final:',num)
'''
# print(list(filter(lambda x:x%3==0,[1,9,55,150,-3,78,28,123])))
# a= filter(lambda x:x%3==0,[1,9,55,150,-3,78,28,123])
# print(next(a))
# print(next(a))
# print(next(a))
#
# def logger(fn):  #这里面是形参
#     def inner(*args,**kwargs):
#         print('called function {}. x={}, y = {}'.format(fn.__name__,*args))
#         ret = fn(*args,**kwargs)    #这里面是参数的结构
#         return ret
#     return inner        #这里面柯里化一下
#
# @logger
# def add(x,y):
#     return x + y
#
# ret = add(4,5)
# print(ret)
from functools import lru_cache
import time
@lru_cache()
def add(x=4,y=5):
    time.sleep(3)
    return x + y
print(1,add(4,5))
print(2,add(4))
print(3,add(y=5))
print(4,add(x=4,y=5))
print(5,add(y=5,x=4))




