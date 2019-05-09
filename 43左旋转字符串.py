# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        if not s or n is None: return ''

        # 内存越界
        if n < 0: return ''

        l = len(s)
        if n >= l:
            n = n % l

        return s[n:] + s[:n]