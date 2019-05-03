# -*- coding:utf-8 -*-
# 测试样例，全是负数（不符合题意?????）
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        l = len(array)
        if l == 1:
            return array
        if l == 0:
            return

        s = 0
        max_sum = None
        for i in range(l):
            s += array[i]

            if max_sum is None:
                max_sum = s
                if s < 0:
                    s = 0
                continue
            if s > max_sum:
                max_sum = s
            if s < 0:
                s = 0

        return max_sum




if __name__ == '__main__':
    a = [-1,-2,-3,-4,-5,-2,-9,-11,-3]
    s = Solution()
    print s.FindGreatestSumOfSubArray(a)