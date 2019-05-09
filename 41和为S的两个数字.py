# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if not array or not tsum: return []

        big = len(array) - 1
        small = 0

        while small < big:
            cur = array[small] + array[big]
            if cur < tsum:
                small += 1
            elif cur > tsum:
                big -= 1
            else:
                return [array[small], array[big]]

        return []






if __name__ == '__main__':
    a = [1,3,4,5,6,7,8]
    s = Solution()
    print s.FindNumbersWithSum(a, 10)