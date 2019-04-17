# 赋值——对象引用
# 例1：
print('............赋值例1..............')
x = 3.14
y = x
print([id(item) for item in [x,y]])
# 输出x和y的地址，地址相同
print(x, y)
x = 1.15
print([id(item) for item in [x,y]])
# 此时地址发生了变化，不再相同
print(x, y)
# 两值也不再相等(不可变对象)

# 例2
print('...........赋值例2...............')
a = [1,3,4]
a1 = a
a2 = a
a1[0] = 100
a2[1] = -1
print(a1, a2)
# 各自的改变都影响到了对方
print([id(x) for x in a1])
print([id(x) for x in a2])
# 两列表地址均相同，是同一个列表(可变对象)

# 浅拷贝
print('.........浅拷贝.................')
m = [100,-100]
b = [1, 2, 3, m]
# 两种浅拷贝的方式
b1 = list(b)
b2 = b.copy()
print(id(b), id(b1), id(b2))
for x,y,z in zip(b, b1, b2):
    print(id(x), id(y), id(z))
b1[2] = -10000000
# 仅有b1发生了改变
b2[3][0] = 1
m[1] = 111
# 均发生了改变
print(b, b1, b2)
# 其中元素地址相同修改任意元素均引起改变

import copy
print('..........深拷贝（可变对象）................')
# 可变对象
a = [[1,2],[3,4],[5,6]]
b = a.copy()
b1 = copy.copy(a)
# 浅拷贝得到b
c = copy.deepcopy(a)
# 深拷贝得到c
print('地址：','原始：  ', id(a), '浅拷贝：  ', id(b), '浅拷贝1：  ', id(b1),'深拷贝：  ', id(c))
# a和b不同
print('_________________子元素__________________')
for x,y,z,d in zip(a,b,b1,c):
    # a和b的子对象相同
    print('子项：','原始：  ', id(x), '浅拷贝：  ', id(y), '浅拷贝1：  ', id(z), '深拷贝：  ', id(d))
a[0][0] = 100
b[0][1] = 100
b1[1][0] = 100
c[1][1] = 100
print(a,b,b1,c)

# 不可变对象
print('..........深拷贝（不可变对象）................')
a = [1,2,3,4]
b = a.copy()
b1 = copy.copy(a)
# 浅拷贝得到b
c = copy.deepcopy(a)
# 深拷贝得到c
print('地址：','原始：  ', id(a), '浅拷贝：  ', id(b), '浅拷贝1：  ', id(b1),'深拷贝：  ', id(c))
print('_________________子元素__________________')
for x,y,z,d in zip(a,b,b1,c):
    # 均相同
    print('子项：','原始：  ', id(x), '浅拷贝：  ', id(y), '浅拷贝1：  ', id(z), '深拷贝：  ', id(d))
a[0] = 100
b[1] = 100
b1[2] = 100
c[3] = 100
print(a,b,b1,c)