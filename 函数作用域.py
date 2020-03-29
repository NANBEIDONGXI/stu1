'''
作用域：
    一个标识符的可见范围，这就是标识符的作用域。一般常说的是变量的作用域
全局作用域：在整个程序运行环境中都可见
局部作用域：在函数，类等内部可见
           局部变量使用范围不能超过其所在的局部作用域
'''
x = 5
def foo():
    global x
    x +=1
    print(x)
foo()  #返回 6

#############
def counter():
    c = [0]
    def inc():
        c[0] +=1
        return c[0]
    return inc    #复杂类型（列表，字典等），地址，引用
foo = counter() #返回 函数inc（函数名） foo= inc inc() =foo()
print(foo(),foo())
c = 100
print(foo()) #上面返回1,2 /n3
