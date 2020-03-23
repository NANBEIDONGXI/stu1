# tail = " ".join([str(i) for i in range(12,0,-1)])
# a = [str(i) for i in range(6)]
# print(tail)
# print(list(tail))
# for i in tail:
#     print(i,end = ' ')
# # print(tail[1])
# print(a)
# b = ' '.join(a)
# print(b)
# print(b[0])
# print(b[1])
# print(b[2])
def fn(x):
    for i in range(x):
        if i > 3:
            return i
    else:
        print('{} is not greater than 3'.format(x))
fn(2)