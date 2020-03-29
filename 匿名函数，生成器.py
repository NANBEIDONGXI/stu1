'''
python借助Lambda表达式构建匿名函数
格式： lambda 参数列表：表达式
       lambda x:x**2
       (lambda x:x**2)(4)  #调用
       foo = lambda x,y:(x+y)**2  #不推荐这么用
       foo(1,2)
       def foo(x,y): #建议使用普通函数
           return (x+y)**3
       foo(2,1)

lambda 表达式（匿名函数）只能写在一行上，被称为单行函数
用途：在高阶函数传参时，使用lambda表达式，往往能简化代码
lambda表达式的 : 后面不能出现赋值表达式（就是不能出现 = ）

print((lambda *args:(x for x in args))(*range(5)))
print((lambda *args:[x+1 for x in args])(*range(5)))
print((lambda *args:{x+2 for x in args})(*range(5)))

[x for x in (lambda *args:map(lambda x:x+1,args))(*range(5))] #高阶函数
[x for x in (lambda *args:map(lambda x:(x+1,args),args))(*range(5))]


生成器generator
生成器指的是生成器对象，可以有生成器表达式得到，也可以使用yield关键字得到一个生成器函数，调用这个函数得到一个生成器对象
生成器函数：
函数体重包含yield语句的函数，返回生成器对象
生成器对象，是一个可迭代对象，是一个迭代器
生成器对象，是延迟计算，惰性求值的

g1 = (i for i in range(5))
print(next(g1))
print(next(g1))
print(g1)

def fn():
    for i in range(5):
        yield i
print(type(fn)) #function
print(type(fn())) #generator
print(next(fn()))
print(next(fn())) #两次返回的值是一样的，每一次都是重新调用
#生成器迭代完后不可回头，要想回头，再拿一个新的生成器对象
#普通的函数调用fn()，函数会立即执行完毕，但是生成器函数可以使用next函数多次执行
#生成器函数等价于生成器表达式，只不过生成器函数可以更加复杂

生成器函数：
1，包含yield语句的生成器函数生成  生成器对象  的时候，生成器函数的函数体不会立即执行
2，next(generator)会从函数的当前位置向后执行到之后碰到的第一个yield语句，会弹出值，并暂停函数执行
3，再次调用next函数，和上一条一样的处理过程
4，没有多余的yield语句能被执行，继续调用next函数，会抛出StopIteration异常

def inc():
    def counter():
        i=0
        while True:
            i += 1
            yield i
    c = counter()
    def _inc():
        return next(c)
    return _inc
    #return lambda :next(c)  上面三行可以改成这一行
g = inc() #可调用对象，函数
print(g())
print(g())
print(g())
'''

#处理递归问题,斐波那契数列
def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b,a+b
        yield a
for x in fib(10):
    print(x)


def fib1():
    x= 0
    y= 1
    while True:
        yield y
        x,y= y,x+y
foo=fib1()
for _ in range(5):
    print(next(foo))