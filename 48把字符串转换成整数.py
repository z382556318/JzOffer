# -*- coding:utf-8 -*-
import re
class Solution:
    def StrToInt(self, s):
        if not s: return 0

        num = r'[0-9]'
        b = 1
        sum = 0
        for i in range(len(s)-1,-1,-1):
            if re.match(num, s[i]):
                sum += b * (int(s[i]) - int('0'))
                b = b * 10
            elif re.match(r'[+-]', s[i]) and i == 0:
                if s[i] == '+':
                    pass
                else:
                    sum = - sum
            else:
                return 0
        return sum

class Solution:
    def StrToInt(self, s):
        if not s: return 0

        numlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        sum = 0
        flag = False
        for i in range(len(s)):
            if s[i] in numlist:
                sum = sum * 10 + numlist.index(s[i])
            elif s[i] == '-' and i == 0:
                flag = True
            elif s[i] == '+' and i == 0:
                pass
            else:
                return 0

        return -sum if flag else sum


if __name__ == '__main__':
    s = Solution()
    print s.StrToInt('111111')