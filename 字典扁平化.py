'''
把一个字典扁平化
源字典   {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}
目标字典 {'a.c':2,'d.e':3,'d.f.g':4,'a.b':1}
用循环或者递归 ，写递归是有套路的

src = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}
target = {}
def flatmap(src:dict,?):
    for k,v in src.items():
        if isinstance(v,(dict,)):#v是字典，则继续递归
            flatmap(v)
        else:
            target[?] = v
    return target

#递归写法有套路的，就按照上面的来
src = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}
target = {}
def flatmap(src:dict,prefix=''):
    for k,v in src.items():#v={'b':1,'c':2}
        if isinstance(v,(dict,)):#v是字典，则继续递归
            prefix = prefix +k +'.'  #'a.'
            flatmap(v,prefix)
            prefix = ''   #这里一定要清理下，不然得到的东西不对
        else:
            target[prefix + k] = v   #'a.b'
    return target
print(flatmap(src))
'''

src = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}

def flatmap(src:dict):
    target = {}
    def _flatmap(src:dict,prefix=''):
        for k,v in src.items():#v={'b':1,'c':2}
            if isinstance(v,(dict,)):#v是字典，则继续递归
                prefix = prefix +k +'.'  #'a.'
                _flatmap(v,prefix)
                prefix = ''    #这里一定要清理下，不然得到的东西不对
                # return flatmap(v,prefix)
            else:
                target[prefix + k] = v   #'a.b'
    _flatmap(src)
    return target
print(flatmap(src))