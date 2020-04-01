'''
求两个字符串的最长公共子串   (最好用矩阵算法）
思考：
s1 = 'abcdefg'
s2 = 'defabcd'

方法一：矩阵算法
让s2的每一个元素，去分别和s1的每一个元素比较，相同就是1，不同就是0，有下面的矩阵

def findit(str1,str2):
    if len(str1) > len(str2):
        str1,str2 = str2,str1
    length1 = len(str1)
    length2 = len(str2)
    #matrix = [[0]*length1]*length2
    matrix = [[0]*length1 for i in range(length2)]
    print(matrix)
    xmax = 0
    xindex = 0
    for i,x in enumerate(str2): #'abc'
        for j,y in enumerate(str1):#'ab'
            if x == y:#两字符相等
                if i == 0 or j == 0:#在边上
                    matrix[i][j] = 1
                else:
                    pre = matrix[i-1][j-1]
                    if pre > 0:
                        matrix[i][j] = pre + 1
                    #记录最大值
                    if matrix[i][j] > xmax:
                        xmax = matrix[i][j]#记录最大值，用于下次比较
                        xindex = j
    print(matrix,xmax,xindex)
    start = xindex + 1 - xmax
    end = xindex + 1
    return str1[start:end]
s1 = 'abcdefg'
s2 = 'defabcd'
print(findit(s1,s2))



方法二：
字符串都是连续的字符，所以才有下面的思路：
思路一：
第一轮
从s1中一次取出1个字符，在s2中查找，看是否能够找到子串
如果没有一个字符在s2中找到，说明就没有公共子串，直接退出。如果找到了至少一个公共子串，则很有可能还有更长的公共子串，可以进入下一轮

第二轮
然后从s1中取连续的2个字符，在s2中查找，看能否找到公共子串，如果没有找到，说明最大公共淄川就是上一轮的随便的哪一个就行了，如果
找到至少一个，则说明公共子串可能还可以再长一些，可以进入下一轮。

改进
其实只要找到第一轮的公共子串的索引，最长公共子串也是从它开始的，所以以后的轮次都从这些索引位置开始，可以减少比较的次数

思路二：
假设s1,s2两个字符串，s1短一些
既然是求最大子串，最长淄川不会超过最短的字符串，先把s1全场作为子串。
在s2中搜索，是否返回正常的index ，正常就找到了最长子串。

没有找到，吧s1按照length-1取多个子串。
在s2中搜索，是否能返回正常的index

注意：
不要一次把s1的所有子串生成，用不了，也不要从最短开始，因为题目要最长的。
但是也要注意，万一他们的公共子串就只有一个字符，或者很少字符的，思路一就会占优势。
'''
def findit(str1,str2):
    if len(str1) > len(str2):
        str1,str2 = str2,str1
    length = len(str1)#str1 最短的字符串
    for sublen in range(length,0,-1):
        for start in range(0,length - sublen + 1):
            substr = str1[start:start + sublen]
            # print(substr)
            if str2.find(substr) > -1:#找不到，返回-1
                return substr

print(findit('abc','abcd'))










