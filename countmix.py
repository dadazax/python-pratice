##Practice1: 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
list = [1, 2, 3, 4]
i=0
for a in list:
    #print(a)
    for b in list:
        for c in list:
            if a != b & b != c & c != a:
                print(100*a + 10*b + c)
                i=i+1
print(i)
