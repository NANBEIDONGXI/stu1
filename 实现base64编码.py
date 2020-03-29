'''
位（bit）、字节（byte）、字符、编码之间的关系
1、位：
数据存储的最小单位。每个二进制数字0或者1就是1个位；

2、字节：
8个位构成一个字节；即：1 byte (字节)= 8 bit(位)；
1 KB = 1024 B(字节)；
1 MB = 1024 KB;   (2^10 B)
1 GB = 1024 MB;  (2^20 B)
1 TB = 1024 GB;   (2^30 B)

3、字符：
a、A、中、+、*、の......均表示一个字符；
一般 utf-8 编码下，一个汉字 字符 占用 3 个 字节；
一般 gbk 编码下，一个汉字  字符  占用 2 个 字节；

位（bit）：是计算机 内部数据 储存的最小单位，11001100是一个八位二进制数。
字节（byte）：是计算机中 数据处理 的基本单位，习惯上用大写  B  来表示,1B（byte,字节）= 8bit（位）
字符：是指计算机中使用的字母、数字、字和符号
ASCIIS码： 1个英文字母（不分大小写）= 1个字节的空间
1个中文汉字 = 2个字节的空间
1个ASCII码 = 一个字节
UTF-8编码：1个英文字符 = 1个字节
             英文标点  = 1个字节
          1个中文（含繁体） = 3个字节
             中文标点 = 3个字节
Unicode编码：1个英文字符 = 2个字节
               英文标点  = 2个字节
            1个中文（含繁体） = 2个字节
                中文标点 = 2个字节

print('中'.encode())  ==> b'\xe4\xb8\xad'
上面是十六进制字符表达形式

print(chr(65))  =>'A'
print(ord('A')  =>65

b:二进制；o:八进制；d:十进制；x:十六进制
在python中，可使用bin(),oct(),hex()返回对应进制的数（相当于十进制转其他进制），均为字符串而且会带有0b,0o,0x前缀
print(bin(128))   =>'0b10000000
print(oct(128))   =>'0o200'
print(hex(128))   =>'0x80'

其他进制转十进制
int('10000000',2)
int('200',8)
int('80',16)

位与：按位相乘
位或：按位相加

从几到几，用什么东西填充
s=b'abcde'
s=bytearray(s)
s[-2:] = b'12'  =>bytearray(b'abc12')
s[-2:] = b'xyz' =>bytearray(b'abcxyz')
s[-3:] = b'12'  =>bytearray(b'abc12')
s[-3:-2] = b'xyz'  =>bytearray(b'abxyz12')
'''
alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def base64encode(src:str):
    target = bytearray()
    if isinstance(src,str):
        _src = src.encode()#字节
    else:
        return
    length = len(_src)
    r = 0  # 余下几个
    for offset in range(0,length,3):
        tripe = _src[offset:offset+3] #b'abc'

        if offset + 3 > length:
            r = 3 - len(tripe)
            tripe = tripe + b'\x00' * r #凑够3个字节，然后从3 变 4 ，24位
            #bytes =>int  只有数字可以进行位运算，这里需要转换成Int
        val = int.from_bytes(tripe,'big')
        for i in range(18,-1,-6):
            if i == 18:   #当第一偏移18位时，只取得六位数字，就不用后面做位与运算,可以少算一次
                index = val >>i
            else:
                index = val >>i & 0x3f  #这里先按位偏移后再跟b'111111' = 0x3f  进行位与运算，可以得到后面六位数
            target.append(alphabet[index])
    #最后得到的结果中的A需要替换为'='
    for i in range(1,r+1):
            target[-i] = 61 #这里的61是ASCII里面’=‘对应的数字61
    # if r: #r=0 不进来
    #     target[-r:] = b'=' * r  #这句可以替代上面的替换循环，从几到几，用什么样的东西填充
    # return target     =>bytearray(b'YQAA')  这里返回的事bytearray,需要转换成字符串
    return bytes(target) #b'YQAA'，不做上面替换=的循环时，返回的就是b'YQAA'
import base64
strlist = ['a','ab','abc','`','马a哥']
for x in strlist:
    print(x)
    print(base64encode(x))
    print(base64.b64encode(x.encode()))
    print()














