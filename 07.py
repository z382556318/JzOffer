# -*- coding:utf-8 -*-
class Solution:
    # 递归调用（时间太长）
    def Fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.Fibonacci(n - 2) + self.Fibonacci(n - 1)


class Solution:
    def Fibonacci(self, n):
        # 动态规划，自底向上
        fes = [0,1]
        while len(fes) <= n:
            fes.append(fes[-1] + fes[-2])
        else:
            return fes[n]
        return fes[-1]


class Solution:
    def Fibonacci(self, n):
        # 动态规划，自底向上，比方法2占用空间更少
        a = 0
        b = 1
        if n <= 1:
            return n
        for i in range(n):
            a, b = b, b + a
        return a



print Solution().Fibonacci(3)