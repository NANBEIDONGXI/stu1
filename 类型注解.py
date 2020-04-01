函数定义的弊端：
python是动态语言，变量随时可以被赋值，且能赋值为不同的类型
python不是静态编译型语言，变量类型是在运行器决定的
动态语言很灵活，但是这种特性也是弊端
def add(x,y):
    return x + y
print(add(4,5))
print(add('hello','world'))#这种开始设计的时候不是准备这样用的，结果别人传错了，还能使用
add(4,'hello')#这种就有问题了

    难发现：由于不做任何类型检查，直到运行期间问题才显现出来，或者线上运行时才能暴露出问题
    难使用：函数的使用者看到函数的时候，并不知道你的函数的设计，并不知道应该传入什么类型的数据

如何解决这种动态语言定义的弊端呢？
    增加文档Documentation string
        这只是一个惯例，不是强制标准，不能要求程序员一定为函数提供说明文档
        函数定义更新了，文档未必同步更新

如果解决这种动态语言定义的弊端呢？
    函数注解
# def add(x:int,y:int) -> int:
#     '''
#
#     :param x: int
#     :param y: int
#     :return: int
#     '''
#     return x + y
# print(help(add))
# print(add(4,5))
# print(add('hell','world'))

def add(x:list,y=int):
    a = x.append(5)          #append就地修改，返回None
    return a
print(add([],23))            #返回None
print(add.__annotations__)  #{'x': <class 'list'>, 'y': <class 'int'>, 'return': None}

函数注解：
    Python 3.5引入
    对函数的参数进行类型注解
    对函数的返回值进行类型注解
    只对函数参数做一个辅助的说明，并不对函数参数进行类型检查
    提供给第三方工具，做代码分析，发现隐藏的bug
    函数注解的信息，保存在__annotations__属性中
add.__annotations__

变量注解：
    python 3.6引入
    i:int = 3     #可以直接这么用，只是起提示说明，不做强制


业务应用：
    函数参数类型检查
    思路：
        函数参数的检查，一定是在函数外
        函数应该作为参数，传入到检查函数中
        检查函数拿到函数传入的实际参数，与形参声明对比
        __annotations__属性是一个字典，其中包括返回值类型的声明。假设要做未知参数的判断，无法和字典中的声明对应。使用inspect模块

    inspect模块
        提供获取对象信息的函数，可以检查函数和类，类型检查


###################################################################
import inspect
def add(x:list,y:str) -> list:
    x.append()
    return x
print(inspect.signature(add))   #==>(x: list, y: str) -> list

sig = inspect.signature(add) #拿到签名（函数签名包含了一个函数的信息，包括函数名，它的参数类型，他所在的类和名称空间及其他信息）
print(sig)                      #==>(x: list, y: str) -> list

params = sig.parameters
print(params)          #==> OrderedDict([('x', <Parameter "x: list">), ('y', <Parameter "y: str">)])

from inspect import Parameter

for i, (k,param) in enumerate(params.items()):
    print(i,k,param)  #下面两行是这句返回的
# 0 x x: list
# 1 y y: str
    param:Parameter   #参数类型
    print(type(params))
    print(param.name,param.default,param.annotation,param.kind) #参数类型可以调用这四样（name,default,annatation,kind)

########################################################
# inspect.isfunction(add)  #检验是否是函数
# inspect.ismethod(add)    #检验是否是类的方法
# inspect.isgenerator((add)) #是否是生成器对象
# inspect.isgeneratorfunction(add) #是否是生成器函数
# inspect.isclass(add)     #是否是类
# inspect.ismodule(inspect) #是否是模块
# inspect.isbuiltin(print)  #判断print是否是内建对象，这里没有调用print()
# 还有很多is函数，需要的时候查阅inspect模块帮助


# Parameter对象：
#     保存在元组中，是只读的
#     name,参数的名字
#     annotation,参数的注解，可能没有定义
#     default,参数的缺省值，可能没有定义
#     empty，特殊的类，用来标记default属性或者注释annotation属性的空值
#     kind,实参如何绑定到形参，就是形参的类型
#         #POSITIONAL_ONLY , 值必须是位置参数提供,这个是没有的，没有仅仅只是位置传参的
#         POSITIONAL_OR_KEYWORD, 值可以作为关键字或者位置参数提供
#         VAR_POSITIONAL ， 可变位置参数，对应*args
#         KEYWORD_ONLY, keyword_only参数，对应*或者*args之后的出现的非可变关键字参数
#         VAR_KEYWORD, 可变关键字参数，对应**kwargs


业务应用：
有函数如下：
def add(xint,y:int=7) -> int:
    return x + y
请检查用户输入是否符合参数注解的要求？
思路：
    调用时，判断用户输入的实参是否符合要求
    调用时，用户感觉上还是在调用add函数
    对用户输入的数据和声明的类型进行对比，如果不符合，提示用户

#############################################################
import inspect
from inspect import Parameter
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
