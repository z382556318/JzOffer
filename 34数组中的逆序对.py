# -*- coding:utf-8 -*-
class Solution:
    # AC25——时间成本太高
    def InversePairs(self, data):
        if not data: return
        res = 0
        for i in range(len(data)-1):
            for j in range(i+1, len(data)):
                if data[j] < data[i]:
                    res += 1

        return res % 1000000007

class Solution:
    # 归并排序
    # AC50——python通不过
    def LikeMergeSort(self, data):
        l = len(data)
        if l == 1:
            return data, 0

        mid = l // 2
        res = []

        a, res_numa = self.LikeMergeSort(data[:mid])
        b, res_numb = self.LikeMergeSort(data[mid:])
        res_num = res_numa + res_numb

        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 and j >= 0:
            if a[i] > b[j]:
                res.insert(0,a[i])
                res_num += j + 1
                i -= 1
            else:
                res.insert(0,b[j])
                j -= 1
        if i < 0:
            for x in range(j, -1, -1):
                res.insert(0, b[x])
        else:
            for y in range(i, -1, -1):
                res.insert(0, a[y])
        return res, res_num

    def InversePairs(self, data):
        a, b = self.LikeMergeSort(data)
        return b

if __name__ == '__main__':
    a = [3, 4, 1, 2,  7, 5, 6,0]
    s = Solution()
    print s.InversePairs(a)