# -*- coding:utf-8 -*-
class Solution:
    # PYTHON需要人工处理边界，且未考虑负数处理
    def Add(self, num1, num2):
        x = lambda a, b: a ^ b
        y = lambda a, b: (a & b) << 1

        res = x(num1, num2)
        carry_bit = y(num1, num2)
        while carry_bit:
            res, carry_bit = x(res, carry_bit) , y(res, carry_bit)
        return res

class Solution:
    def Add(self, num1, num2):
        x = lambda a, b: (a ^ b) & 0xFFFFFFFF
        # 需要加括号：& 优先级更高
        y = lambda a, b: ((a & b) << 1) & 0xFFFFFFFF

        res = x(num1, num2)
        carry_bit = y(num1, num2)
        while carry_bit:
            res, carry_bit = x(res, carry_bit), y(res, carry_bit)
        return res if res <= 0x7FFFFFFF else ~(res^0xFFFFFFFF)

if __name__ == '__main__':
    s = Solution()
    print s.Add(-5,20)
