# -*- coding:utf-8 -*-
# 测试样例：空？
# 大数问题——字符串的比较
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers: return ''
        # 方便的转化方式
        new = list(map(str, numbers))
        y = lambda s1, s2: cmp(s1+s2, s2+s1)
        # 不宜用int(s1+s2)形式
        new.sort(cmp=y)
        # 避免[0,0,0,0]的测试样例
        return ''.join(new).lstrip('0') or '0'

class Solution:
    def QuickSort(self, numbers):
        y = lambda s1, s2: cmp(s1 + s2, s2 + s1)
        right = len(numbers) - 1
        left = 0
        stack = [left, right]
        while stack:
            end = right = stack.pop()
            start = left = stack.pop()
            key = numbers[left]
            while left < right:
                while y(numbers[right],key) >= 0 and right > left:
                    right -= 1
                numbers[left] = numbers[right]
                while y(numbers[left], key) <= 0 and right > left:
                    left += 1
                numbers[right] = numbers[left]
            else:
                numbers[left] = key
                if left-1 > start:
                    stack.extend([start, left-1])
                if left+1 < end:
                    stack.extend([left+1, end])
        return numbers

    def PrintMinNumber(self, numbers):
        if not numbers: return ''
        # 方便的转化方式
        numbers = list(map(str, numbers))

        return ''.join(self.QuickSort(numbers)).lstrip('0') or '0'


if __name__ == '__main__':
    a = [11,9,921]
    s = Solution()
    print s.QuickSort(a)
    print s.PrintMinNumber(a)