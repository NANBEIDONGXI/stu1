def showconfig(**kwargs):
    # print(type(kwargs))
    # print(kwargs)
    # kwargs['a']= 1000
    # print(kwargs)
    for k,v in kwargs.items():
        print('{}={}'.format(k,v))

showconfig(host='localhost',port=80,username='wayne')

