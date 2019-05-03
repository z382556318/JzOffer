# -*- coding:utf-8 -*-
# 快排的思想——如何找出第K+1个数（随便找，不够填，够了减）
# 堆排序——排K个
class Solution:
    # 堆排序加改变元素位置(时间复杂度O(NlogN)
    def heapAdjust(self, array, start, end):
        root = start

        while True:
            left = 2 * root + 1
            if left > end: break
            if left < end and array[left] < array[left+1]:
                left += 1
            if array[root] < array[left]:
                array[root], array[left] = array[left], array[root]
                root = left
            else:
                break

    def heapSort(self, array):
        last = len(array) - 1
        last_leaf = (last-1) // 2

        # 初始化堆
        for i in range(last_leaf, -1, -1):
            self.heapAdjust(array, i, last)

        for end in range(last, 0, -1):
            array[0], array[end] = array[end], array[0]
            self.heapAdjust(array, 0, end - 1)
        return

    def GetLeastNumbers_Solution(self, tinput, k):
        if k <= 0 or k > len(tinput):
            return []
        self.heapSort(tinput, k)
        return tinput[:k]

class Solution:
    # 大顶堆：维护一个k个元素的大顶堆，若大于堆顶则跳过，若小于堆顶则替换堆顶，并调整堆。
    # 可以维护一个新的堆栈，避免改变原来的数据
    def heapAdjust(self, array, start, end):
        root = start
        while True:
            left = 2 * root + 1
            if left > end: break
            if left < end and array[left] < array[left+1]:
                left += 1
            if array[root] < array[left]:
                array[root], array[left] = array[left], array[root]
                root = left
            else:
                break

    def GetLeastNumbers_Solution(self, tinput, k):
        if k <= 0 or k > len(tinput):
            return []

        last_no_leaf = k // 2 - 1
        for i in range(last_no_leaf, -1, -1):
            self.heapAdjust(tinput, i, k - 1)

        for j in range(k, len(tinput)):
            if tinput[j] >= tinput[0]:
                pass
            else:
                tinput[0] = tinput[j]
                self.heapAdjust(tinput, 0, k - 1)

        return sorted(tinput[:k])





if __name__ == '__main__':
    a = [1,2,3,2,4,2,5,2,3]
    s = Solution()
    print s.GetLeastNumbers_Solution(a,7)