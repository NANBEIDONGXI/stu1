
def logger(fn):  #这里面是形参           这样用装饰器的话，logger函数需要写在前面，需要先定义，不然会报错
    def wapper(*args,**kwargs):  #
        '''
        this is wrapper function
        这是函数文档，函数调用__doc__会显示
        :param args:
        :param kwargs:
        :return:
        '''
        print('called function {}. x={}, y = {}'.format(fn.__name__,*args))
        ret = fn(*args,**kwargs)    #这里面是参数的结构
        return ret
    return wapper        #这里面柯里化一下

@logger    #这里的@logger  相当于  add = logger(add)   可以看上面的line34~36   =左边的add就是wapper
def add(x,y):
    '''
    this is add function
    :param x:
    :param y:
    :return:
    '''
    return x + y
print(add.__name__)     #这里有装饰器，所以add是wrapper函数
print(add.__doc__)

#但是别用的时候不知道函数被包装过的，就是想知道add函数本身的一些名字，文档等内容，所以需要修改下
#所以需要修改下


########################################################################################################
def logger(fn):  #这里面是形参           这样用装饰器的话，logger函数需要写在前面，需要先定义，不然会报错
    def wrapper(*args,**kwargs):  #
        '''
        this is wrapper function
        这是函数文档，函数调用__doc__会显示
        :param args:
        :param kwargs:
        :return:
        '''
        print('called function {}. x={}, y = {}'.format(fn.__name__,*args))
        ret = fn(*args,**kwargs)    #这里面是参数的结构
        return ret
    wrapper.__name__ = fn.__name__    #在这里把名称跟文档替换下
    wrapper.__doc__ = fn.__doc__
    return wrapper        #这里面柯里化一下

@logger    #这里的@logger  相当于  add = logger(add)   可以看上面的line34~36   =左边的add就是wapper
def add(x,y):
    '''
    this is add function
    :param x:
    :param y:
    :return:
    '''
    return x + y
print(add.__name__)     #这里有装饰器，所以add是wrapper函数
print(add.__doc__)

################################################################3


def logger(fn):  #这里面是形参           这样用装饰器的话，logger函数需要写在前面，需要先定义，不然会报错
    def copy_properties(src,dest):            #把函数抽取出来
        dest.__name__ = src.__name__
        dest.__doc__ = src.__doc__

    def wrapper(*args,**kwargs):  #
        '''
        this is wrapper function
        这是函数文档，函数调用__doc__会显示
        :param args:
        :param kwargs:
        :return:
        '''
        print('called function {}. x={}, y = {}'.format(fn.__name__,*args))
        ret = fn(*args,**kwargs)    #这里面是参数的结构
        return ret
    copy_properties(fn,wrapper)
    return wrapper        #这里面柯里化一下

@logger    #这里的@logger  相当于  add = logger(add)   可以看上面的line34~36   =左边的add就是wapper
def add(x,y):
    '''
    this is add function
    :param x:
    :param y:
    :return:
    '''
    return x + y
#########################################################################################################f
from functools import update_wrapper ,wraps
def copy_properties(src):            #把函数柯里化一下
    def _copy(dest):       #这里的dest，就是下面对应的wrapper
        dest.__name__ = src.__name__
        dest.__doc__ = src.__doc__
        return dest        #这里需要加上这一句，不然的话，line100 ,wrapper= copy_properties(fn)(wrapper)  ==> _copy(wrapper),这里返回值就会是None
    return _copy
def logger(fn):  #这里面是形参           这样用装饰器的话，logger函数需要写在前面，需要先定义，不然会报错
    @copy_properties(fn)    #如果不加(fn)的话    wrapper = copy_properties(wrapper)      #copy_properties(fn)(wrapper) = _copy(wrapper) 这是的返回值不能是None
                            #这里如果要改为上一行后面的，需要加上fn这个函数
    def wrapper(*args,**kwargs):  #
        '''
        this is wrapper function
        这是函数文档，函数调用__doc__会显示
        :param args:
        :param kwargs:
        :return:
        '''
        print('called function {}. x={}, y = {}'.format(fn.__name__,*args))
        ret = fn(*args,**kwargs)    #这里面是参数的结构
        return ret
    #copy_properties(fn)(wrapper)
    update_wrapper(wrapper,fn)
    return wrapper        #这里面柯里化一下

@logger    #这里的@logger  相当于  add = logger(add)   可以看上面的line34~36   =左边的add就是wapper
def add(x,y):
    '''
    this is add function
    :param x:
    :param y:
    :return:
    '''
    return x + y

ret = add(4,5)
print(ret)
print(add.__name__)
print(add.__doc__)
##################################################################################################################
from functools import update_wrapper ,wraps
def copy_properties(src):            #把函数柯里化一下
    def _copy(dest):       #这里的dest，就是下面对应的wrapper
        dest.__name__ = src.__name__
        dest.__doc__ = src.__doc__
        return dest        #这里需要加上这一句，不然的话，line100 ,wrapper= copy_properties(fn)(wrapper)  ==> _copy(wrapper),这里返回值就会是None
    return _copy
def logger(fn):  #这里面是形参           这样用装饰器的话，logger函数需要写在前面，需要先定义，不然会报错
    # @copy_properties(fn)    #如果不加(fn)的话    wrapper = copy_properties(wrapper)      #copy_properties(fn)(wrapper) = _copy(wrapper) 这是的返回值不能是None
    @wraps(fn)        #wrapper = wraps(fn)(wrapper)    wrapper  =wrapper
    def wrapper(*args,**kwargs):  #
        '''
        this is wrapper function
        这是函数文档，函数调用__doc__会显示
        :param args:
        :param kwargs:
        :return:
        '''
        print('called function {}. x={}, y = {}'.format(fn.__name__,*args))
        ret = fn(*args,**kwargs)    #这里面是参数的结构
        return ret
    #copy_properties(fn)(wrapper)
    # update_wrapper(wrapper,fn)       #前面用了@wraps装饰器后，这一句就不用了
    return wrapper

@logger    #这里的@logger  相当于  add = logger(add)   可以看上面的line34~36   =左边的add就是wapper
def add(x,y):
    '''
    this is add function
    :param x:
    :param y:
    :return:
    '''
    return x + y

ret = add(4,5)
print(ret)
print(add.__name__)
print(add.__doc__)

# 通过copy_properties 函数将被包函数的属性覆盖掉包装函数
# 凡是被装饰的函数都需要复制这些属性，这个函数很通用
# 可以将负指数型的函数构建成装饰器函数，带参装饰器





