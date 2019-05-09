# -*- coding:utf-8 -*-
import time
import random
class Solution:
    def GetNumberOfK(self, data, k):
        if data is None or k is None: return 0

        # 寻找起点
        start = left = 0
        end = right = len(data) - 1
        first = None
        while left <= right:
            mid = left + (right - left) // 2
            if data[mid] < k:
                left = mid + 1
            elif data[mid] > k:
                right = mid - 1
            else:
                if mid == 0:
                    first = 0
                    break
                elif data[mid - 1] != k:
                    first = mid
                    break
                else:
                    right = mid - 1

        if first is None:
            return 0

        left = start
        right = end
        last = None
        while left <= right:
            mid = left + (right - left) // 2
            if data[mid] < k:
                left = mid + 1
            elif data[mid] > k:
                right = mid - 1
            else:
                if mid == end:
                    last = end
                    break
                elif data[mid + 1] != k:
                    last = mid
                    break
                else:
                    left = mid + 1

        return last - first + 1



class Solution2:
    def GetNumberOfK(self, data, k):
        return data.count(k)

if __name__ == '__main__':
    a = sorted([random.randint(1,10) for i in range(20)])
    print a
    # a = [1, 1, 1, 1, 2, 2, 4, 4, 4, 5, 6, 6, 6, 6, 7, 7, 8, 9, 10, 10]
    s = Solution()
    print s.GetNumberOfK(a, 3)



