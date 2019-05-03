# -*- coding:utf-8 -*-
# 测试用例：空数组，全部未超过一般

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # 哈希表
        if len(numbers) == 0:
            return 0

        if len(numbers) == 1:
            return numbers[0]

        sign = len(numbers) / 2
        data = {}
        for i in numbers:
            if i in data.keys():
                data[i] += 1
                if data[i] > sign:
                    return i
            else:
                data[i] = 1
            print data

        return 0

class Solution:
    def partition(self, numbers, left, right):
        if left >= right: return left

        key = numbers[left]

        while left < right:
            while numbers[right] >= key and left < right:
                right -= 1
            numbers[left] = numbers[right]

            while numbers[left] <= key and left < right:
                left += 1
            numbers[right] = numbers[left]
        numbers[left] = key
        return left

    def quickSort(self, numbers, left, right):
        if left < right:
            q = self.partition(numbers, left, right)

            self.quickSort(numbers, left, q)
            self.quickSort(numbers, q + 1, right)


    def MoreThanHalfNum_Solution(self, numbers):
        # 排序
        if len(numbers) == 0:
            return 0
        if len(numbers) == 1:
            return numbers[0]

        self.quickSort(numbers,0,len(numbers)-1)
        index = int(len(numbers)/2)
        # 向上取整：int((A+B-1)/B) = ((A-1)/B + 1)

        count = 0
        for i in range(len(numbers)):
            if numbers[i] == numbers[index]:
                count += 1

        if count > index+1:
            return numbers[index]
        else:
            return 0

import collections
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        tmp = collections.Counter(numbers)
        x = len(numbers)/2
        for k, v in tmp.items():
            if v > x:
                return k
        return 0

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if len(numbers) == 0:
            return 0
        if len(numbers) == 1:
            return numbers[0]

        key = numbers[0]
        count = 1
        for i in range(1, len(numbers)):
            if numbers[i] == key:
                count += 1
            else:
                count -= 1
            if count == 0:
                key = numbers[i]
                count = 1

        time = 0
        for i in range(len(numbers)):
            if key == numbers[i]:
                time += 1


        if 2 * time > len(numbers):
            return key
        else:
            return 0


if __name__ == '__main__':
    a = [1,2,3,2,4,2,5,2,3]
    s = Solution()
    print s.MoreThanHalfNum_Solution(a)
