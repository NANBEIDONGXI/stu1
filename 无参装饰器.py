def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def a(x,y,z):
    pass
def b(m,n,*args,x,y,**kwargs):
    pass
# def logger(fn,x,y):
#     print('called function {}. x={}, y = {}'.format(fn.__name__,x,y))
#     ret = fn(x,y)
#     return ret

def logger(fn,*args,**kwargs):  #这里面是形参
    print('called function {}. x={}, y = {}'.format(fn.__name__,x,y))
    ret = fn(*args,**kwargs)    #这里面是参数的结构
    return ret

def logger(fn):  #这里面是形参
    def inner(*args,**kwargs):
        print('called function {}. x={}, y = {}'.format(fn.__name__,*args))
        ret = fn(*args,**kwargs)    #这里面是参数的结构
        return ret
    return inner        #这里面柯里化一下

# logger(add(4,5))  转换成了  logger(add)(4,5)

fn = logger(add)
ret = fn(4,5)
print(ret)

add = logger(add)   #先执行= 右边的，logger里面的fn把函数add记住了，logger用到了闭包，然后add被重新定义了
ret = add(4,5)      #这里的add(4,5) 还是指的上一步的被fn记住的函数add,这里的add可以晒任何变量
print(ret)

#这里用到了嵌套函数，作用域，还有讲到的闭包，还用到了函数定义的本质，还用到了可变参数，以及参数解构。

# print('result = {}'.format(logger(add,4,5)))
# print('result = {}'.format(logger(sub,4,5)))
# print('result = {}'.format(logger(b,4,5,6,7,x=10,y=11)))


#分割线分割线分割线分割线分割线分割线分割线分割线分割线分割线分割线分割线分割线分割线分割线分割线分割线分割线
#下面是python里面的装饰器

def logger(fn):  #这里面是形参           这样用装饰器的话，logger函数需要写在前面，需要先定义，不然会报错
    def wapper(*args,**kwargs):  #
        print('called function {}. x={}, y = {}'.format(fn.__name__,*args))
        ret = fn(*args,**kwargs)    #这里面是参数的结构
        return ret
    return wapper        #这里面柯里化一下

@logger    #这里的@logger  相当于  add = logger(add)   可以看上面的line34~36   =左边的add就是wapper
def add(x,y):
    return x + y

ret = add(4,5)  #这里的add，是logger函数返回的wapper
print(ret)
#上面返回
# ==>called function add. x=4, y = 5
# ==>9
#wapper 包装纸，wapper 是包装者， @logger下面的add函数就是被包装者

装饰器（无参）：
    它是一个函数
    函数作为它的形参
    返回值也是一个函数
    可以使用@functionname方式，简化调用
    注：此处装饰器的定义只是就目前所学的总结，并不准确，只是方便理解

装饰器和高阶函数：
    装饰器是高阶函数，但装饰器是对传入函数的功能的装饰（功能增强）
















