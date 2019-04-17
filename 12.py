# -*- coding:utf-8 -*-
class Solution1:
    def Power(self, base, exponent):
        # write code here
        return pow(base,exponent)

class Solution2:
    def Power(self, base, exponent):
        flag = False
        if base == 0:
            return False
        if exponent < 0:
            flag = True
            exponent = abs(exponent)
        result = 1
        for i in range(exponent):
            result = result * base
        return 1 / result if flag else result

class Solution3:
    # 递归调用
    def Power(self, base, exponent):
        if base == 0:
            return False
        elif exponent == 0:
            return 1

        if exponent == 1:
            return base
        elif exponent == -1:
            return 1 / base

        if exponent % 2 == 0:
            return self.Power(base, exponent / 2) ** 2
        else:
            return self.Power(base, (exponent - 1) / 2) ** 2 * base

class Solution3:
    # 快速幂算法
    def Power(self, base, exponent):
        if base == 0:
            return False
        elif exponent == 0:
            return 1

        if exponent < 0:
            flag = True
            exponent = abs(exponent)
        else:
            flag = False

        result = 1
        while (exponent != 0):
            if (exponent & 1 == 1):
                result *= base
            base *= base
            exponent = exponent >> 1
        return 1 / result if flag else result


print Solution3().Power(2,3)