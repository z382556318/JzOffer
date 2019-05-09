# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        ans = n
        temp = ans and self.Sum_Solution(n - 1)
        ans = ans + temp
        return ans


# #1.(0、''、[]、()、{}、None、False) and 任何数等于假
# >>> 0 and 2
# 0
# >>> '' and 3
# ''
# >>> [] and 4
# []
# >>> () and 5
# ()
# >>> {} and 6
# {}
# >>> None and 7
#
# >>> False and 8
# False
# #2.如果表达式中某个值为假，则返回第一个假值
# >>> 0 and 1 and 2
# 0
#
# #3.所有值都为真，则返回最后一个真值
# >>> 2 and 3
# 3
# >>> 2 and 3 and 4
# 4
#
# #现在已经很好理解下面的运算结果了
# >>> 0 and 1       #假 and 真    =>假
# 0
# >>> 0 and 0       #假 and 假    =>假
# 0
# >>> 1 and 0       #真 and 假    =>假
# 0
# >>> 1 and 1       #真1 and 真2  =>真2
# 1
class Solution:
    def Sum_Solution(self, n):
        return reduce(lambda x, y: x+y, range(1, n+1))

class Solution:
    def Sum_Solution(self, n):
        return self.helper(n)

    def helper(self, n):
        try:
            1 / n
            return n + self.helper(n - 1)
        except:
            return 0

if __name__ == '__main__':
    s = Solution()
    print s.Sum_Solution(10)