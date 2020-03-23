# def ad(x,y,*args):
#     print(x,y,args)
#     return  max(x,y,*args),min(x,y,*args)
# print(ad(2,6,1,2,23))
# 编写一个函数，接受一个参数n,n为正整数，要求数字必须对齐
#思路一：一行行打印，前面追加空格，每一个空格的宽度等于数字字符串的宽度
# def triangle(n): #n=3
#     for i in range(1,n+1):
#         for j in range(n,0,-1):
#             # print('{:>40}'.format(i+1),end = ' ')
#             if i < j:
#                 print(' '*len(str(j)),end= ' ')
#             else:
#                 print(j,end=' ')
#         print('')
# triangle(9)

#思路二：右对齐方式，最大问题是不知 道最后一行有多长
# def triangle(n):
#     tail = " ".join([str(i) for i in range(n,0,-1)])
#     width = len(tail)
#     for i in range(n):
#         print('{:>{}}'.format(" ".join([str(j) for j in range(i,0,-1)]),width))
#     print(tail)
# triangle(12)

#思路三：基于思路二，每一行不重新计算，直接用tail得到
# def triangle(n):
#     tail = " ".join([str(i) for i in range(n,0,-1)])
#     width = len(tail)
#     print(type(tail))
#     print(tail)
#     start = -1
#     step = 2
#     points = {10*i for i in range(1,5)} #与其算好两位数，三位数，还不如算好临界值，这是一个set，10,100,1000
#     for i in range(1,n+1):
#         print('{:>{}}'.format(tail[start:],width))
#         if i+1 in points:#当i=9时，i+1 = 10,步长+1，以此类推
#             step +=1
#         start = start - step
# triangle(20)
#下三角思路：找到空格，然后直接切
# def tri(n):
#     tail = ' '.join([str(i) for i in range(n,0,-1)])
#     print(tail)
#     for i in range(len(tail)):
#         if tail[i] == ' ':
#             print(' '*i,tail[i+1:])
# tri(12)
#由此得到上三角的另外一种思路：
'''             1
              2 1
            3 2 1
          4 3 2 1
        5 4 3 2 1
      6 5 4 3 2 1
    7 6 5 4 3 2 1
  8 7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1
'''
def tri(n):
    tail = ' '.join(str(i) for i in range(n,0,-1))
    width = len(tail)
    for i in range(-1,-width-1,-1):
        if tail[i] == ' ':
            print(' '*(width+i),tail[i+1:])
    print(tail)
tri(9)