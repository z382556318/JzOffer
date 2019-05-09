# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum <= 0: return []
        res = []
        for i in range(1, tsum):
            sum = tmp = i
            while sum < tsum:
                tmp += 1
                sum += tmp
            else:
                if sum == tsum:
                    res.append(range(i, tmp+1))
                else:
                    continue

        return res

class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum <= 0 or not tsum: return []
        res = []
        small = 1
        while small <= (tsum//2):
            big = small + 1
            cur = big + small
            while cur != tsum and small < big:
                if cur < tsum:
                    big += 1
                    cur += big
                elif cur > tsum:
                    cur -= small
                    small += 1
            if small != big:
                res.append(range(small, big+1))
            small += 1

        return res

if __name__ == '__main__':
    s = Solution()
    print s.FindContinuousSequence(100)