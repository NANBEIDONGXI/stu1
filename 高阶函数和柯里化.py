'''
高阶函数：
1,First Class Object
    函数在python中是一等公民
    函数也是对象，可调用的对象
    函数可以作为普通变量，参数，返回值等等
2,高阶函数
    数学概念y = g(f(x))
    在数学和计算机科学中，高阶函数应当是至少满足下面一个条件的函数
        接受一个或东哥函数作为参数
        输出一个函数

def counter(base):
    def inc(step=1):
        base += step
        return base
    return inc

分析：
上面函数counter是不是一个高阶函数  =》是高阶函数
上面代码有没有什么问题？怎么改进    =》base += step  这里的base成了新的局部变量，但是没有定义，出错了，在这句前面加上 nonlocal base
f1 = counter(5)
f2 = counter(5)
f1 == f2   =>返回 False   这里返回的内容现在所学的不能比较，就相当于比较内存地址，内存地址不同
f1 is f2   =>返回 False    这里就是比较内存地址


自定义sort函数
排序问题：
    仿照内建函数sorted，请自行实现一个sort函数（不能使用内建函数），能够为列表元素排序
思路：
    内建函数sorted函数是返回一个新的列表，可以设置升序或降序，可以设置一个排序的函数。
    自定义的sort函数也要实现这个功能
    新建一个列表，遍历原列表，和新列表的值一次比较决定如何插入到新列表中

思考：
    sorted函数的实现原理，扩展到map. filter函数的实现原理
  

'''
def sort(iterable,reverse = False):
    newlist = []
    for x in iterable:
        for i,y in enumerate(newlist):
            flag = x > y if reverse else x < y
            if flag:
                newlist.insert(i,x)
                break
        else:
            newlist.append(x)
    return newlist
print(sort([1,2,0],reverse =True))

#上面改进下
def compare(a,b):    #把两个元素比较定义个函数，然后放到外面，然后传参到sort函数里，现在传参传了函数，是高阶函数
    return a > b
def sort(iterable,reverse = False,key = compare):
    newlist = []
    for x in iterable:
        for i,y in enumerate(newlist):
            flag = key(x,y) if reverse else not key(x,y)
            if flag:
                newlist.insert(i,x)
                break
        else:
            newlist.append(x)
    return newlist

#再用lambda函数表示大小比较
# def compare(a,b):    #把两个元素比较定义个函数，然后放到外面，然后传参到sort函数里，现在传参传了函数，是高阶函数
#     return a > b
def sort(iterable,reverse = False,key = lambda a,b: a>b):  #再用lambda函数表示大小比较
    newlist = []
    for x in iterable:
        for i,y in enumerate(newlist):
            flag = key(x,y) if reverse else not key(x,y)
            if flag:
                newlist.insert(i,x)
                break
        else:
            newlist.append(x)
    return newlist

def sort(iterable,reverse = False,key = str):  #lambda x:str(x),形参key相当于右边lambda函数，但是直接key =str简单些
    newlist = []
    for x in iterable:
        for i,y in enumerate(newlist):
            flag = key(x) > key(y) if reverse else key(x)<key(y)
            if flag:
                newlist.insert(i,x)
                break
        else:
            newlist.append(x)
    return newlist


内建函数——高阶函数：
sorted(iterable[,key][,reverse])
    排序
filter(function,iterable) -->filter object
    过滤数据
map(func,*iterables) -->map object
    映射

sorted(iterable[,key][,reverse])排序
    返回一个新的列表，对一个可迭代对象的所有元素排序，排序规则为key定义的函数，reverse表示是否排序翻转
sorted(lst,key = lambda x:6-x) #返回新列表
list.sort(key = lambda x:6-x) #就地修改

filter(function,iterable)
    过滤可迭代对象的元素，返回一个迭代器
    function一个具有一个参数的函数，返回bool
    例如，过滤出数列中能被3整除的数字
        list(filter(lambda x:x%3==0,[1,9,55,150,-3,78,28,123]))

map(func,*iterables)  -->map object
    对多个可迭代对象的元素按照指定的函数进行映射，返回一个迭代器
        lsit(map(lambda x:2*x + 1,range(5)))
        dict(map(lambda x:(x%5,x),range(500)))


# 柯里化Currying:
#     指的是将原来接受两个参数的函数编程新的接受一个参数的函数的过程。新的函数返回一个以原有第二个参数为参数的函数
#     z = f(x,y)   转换成  z = f(x)(y)
def add(x,y): #f(x,y)
    return x + y

add(4,5)
#转换为下面这样的，就是柯里化
def add(x):  #f(x)(y)
    def fn(y):
        return x + y
    return fn
add(4)(5)

通过嵌套函数就可以把函数转化为柯里化函数

