# -*- coding:utf-8 -*-
import collections
class Solution:
    def IsContinuous(self, numbers):
        if len(numbers) < 5 or numbers is None: return False

        # 插入排序
        for i in range(1, len(numbers)):
            tmp = numbers[i]
            j = i - 1
            while numbers[j] > tmp and j >= 0:
                numbers[j+1] = numbers[j]
                j -= 1
            numbers[j+1] = tmp

        zeronum = 0
        # zeronum = collections.Counter(0)
        for x in numbers:
            if x == 0:
                zeronum += 1
            else:
                break

        for i in range(zeronum, len(numbers)-1):
            sign = numbers[i+1] - numbers[i]
            if sign == 0:
                return False
            elif sign > 1:
                zeronum -= (sign - 1)
                if zeronum < 0:
                    return False
            else:
                pass

        return True

if __name__ == '__main__':
    a = [1,2,3,5,0]
    s = Solution()
    print s.IsContinuous(a)