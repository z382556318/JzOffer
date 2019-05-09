# -*- coding:utf-8 -*-
# 样例：全两次，仅一个一次，只有两个一次
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if len(array) <= 1: return []

        tmp = array[0]
        for i in range(1, len(array)):
            tmp ^= array[i]

        if tmp < 0:
            tmp &= 0xffffffff
        high = 1
        while tmp:
            tmp, high = tmp >> 1, high << 1

        a, b = 0, 0
        for i in range(len(array)):
            if array[i] % high // (high >> 1) == 1:
                a ^= array[i]
            else:
                b ^= array[i]

        return [a, b]

if __name__ == '__main__':
    a = [2, 3, 3, 2, -5, 6]
    s = Solution()
    print s.FindNumsAppearOnce(a)
