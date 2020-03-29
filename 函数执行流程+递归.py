'''
函数执行流程

http://pythontutor.com/visualize.html#mode=edit

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

全局帧中生成foo1,foo2,foo3,main函数对象
栈：后进先出原则
main函数调用
main中查找内建函数print 压栈，将常量字符串压栈，调用函数，弹出栈顶

main中全局查找函数foo1压栈，将常量100,101压栈，调用函数foo1,创建栈帧。
print函数压栈，字符串和变量b,b1压栈，调用函数，弹出栈顶，返回值

main中全局查找foo2函数压栈，将常量200压栈，调用foo2,创建栈帧。foo3函数压栈，变量c引用压栈，
调用foo3，创建栈帧。foo3完成print函数调用后返回。foo2回复调用，执行print后，返回值。main中
foo2调用结束弹出栈顶。main继续执行print函数调用，弹出栈顶，main函数返回。

函数执行要压栈，函数执行完后要弹出，
'''

'''
递归 Recursion
函数直接或者间接调用自身就是 递归
递归需要有边界条件.递归前进段，递归返回段
递归一定要有边界条件
当边界条件不满足的时候，递归前进
当边界条件满足的时候，递归返回

fib
循环的写法
a=0
b=1
n=4
for i in range(n):
    a, b = b, a+b
    print(a)
或者用递归
def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
下面是递归的写法
def fib(n):
    if n==0:
        return 0
    if n < 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
for i in range(1,11):
    print(fib(i))
    
def fib(n):
    return 1 if n<3 else fib(n-1) +fib(n-2)
上面这个效率太低了
改进后,下面这个效率其实不差
def fib3(n,a=0,b=1):
    if n<3:
        return a+b
    else:
        a , b= b,a+b
        return fib3(n-1,a,b)     
        
def fib(n,pre=0,cur=1):
    pre, cur= cur, pre+cur
    if n==0:
        return pre
    return fib(n-1,pre,cur)
fib(n)   
#改进后，上面的fib函数和循环的思想类似，参数n是边界条件，用n来计数，上一次的计算结果直接作为
函数的实参，效率很高，和循环比较，性能相近，所以并不是说递归一定效率低下。但是递归有深度限制。

递归总结：
1，递归是一种很自然的表达，符合逻辑思维
2，递归相对运行效率低下，每一次调用函数都要开辟栈帧
3，递归有深度限制，如果递归层次太深，函数反复压栈，栈内存很快就溢出了
4，如果是有限次数的递归，可以使用递归调用，或者使用循环代替，循环代码稍微复杂一些，但是只要不是死循环，可以多次迭代直至算出结果
5，绝大多数递归，都可以使用循环实现
6，及时递归代码很简洁，但是  能不用则不用递归


#递归练习题
#求n的阶乘
def fac1(n):
    if n==1:
        return 1
    return n * fac1(n-1)
print(fac1(4))

def fac2(n,fac=1):
    if n==1:
        return fac
    fac = fac * n
    return fac2(n-1,fac)
print(fac2(3))

#解决猴子吃桃问题
#猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，有多吃了一个。第二天早上又将剩下的桃子吃了一半，然后又多吃了一个，以后每天早上都吃剩下的一半零一个，
#到第10天想吃的时候只剩下一个桃子了，问原来总共摘了多少个桃子

def peach(days=10):
    if days==1:
        return 1
    return (peach(days-1)+1)*2
print(peach())

def peach(days=10):
    if days==10:
        return 1
    return (peach(days+1)+1)*2
print(peach())
'''
#讲一个数逆序放入列表中，例如1234 => [4,3,2,1]
#递归取字符
date = str(1234)
def revert(x):
    if x ==-1:
        return []
    return [date[x]] + revert(x-1)
print(revert(len(date)-1))

#递归切片
date = str(1234)
def revert2(x,target=[]):
    if x:
        target.append(x[-1])
        revert2(x[:-1])
    return target
print(revert2(date))

#使用数字整除取模递归
def revert3(x,target=None):
    if target is None:
        target = []
    x,y = divmod(x,10)
    target.append(y)
    if x == 0:
        return target
    return revert3(x,target)
print(revert3(123045))

