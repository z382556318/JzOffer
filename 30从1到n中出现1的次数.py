# -*- coding:utf-8 -*-
# class Solution:
#     # 时间复杂度：O（Nlog10N）
#     def NumberOf1Between1AndN_Solution(self, n):
#         if n < 1:
#             return 0
#         if n < 10:
#             return 1
#
#         one_num = 1
#         d = 10
#         for i in range(10,n + 1):
#             if i >= 10 * d:
#                 tmp = d = d*10
#             else:
#                 tmp = d
#
#             while True:
#                 a = i % d
#                 b = i // d
#
#                 if b == 1:
#                     one_num += 1
#                 d = d / 10
#                 if a != 0:
#                     i = a
#                 else:
#                     d = tmp
#                     break
#
#         return one_num

# 递归
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        if n < 1:
            return 0
        str_n = str(n)
        m = len(str_n)
        res = 0
        for i in range(m):
            base = 10 ** (m - i - 1)
            sign = float(n) / (10 * base)
            int_sign = int(sign)
            if sign - int_sign >= 0.2:
                res += base * (int_sign + 1)
            elif sign == int_sign:
                res += base * int_sign
            else:
                res += base * int_sign + n - int(sign * 10) * base + 1
        return res

if __name__ == '__main__':
    s = Solution()
    print s.NumberOf1Between1AndN_Solution(21345)