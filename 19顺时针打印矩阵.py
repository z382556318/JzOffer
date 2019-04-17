# -*- coding:utf-8 -*-
# 思路：四个为一个周期（序号变化方式不同）
# 测试样例：空矩阵，一维矩阵
import random

class Solution:
    def oneCircle1(self, lenstart, lenend, widstart, widend, matrix):
        res = []
        for i in range(lenstart, lenend + 1):
            res.append(matrix[widstart][i])
        for j in range(widstart + 1, widend + 1):
            res.append(matrix[j][lenend])
        for i in range(lenend - 1, lenstart - 1, -1):
            res.append(matrix[widend][i])
        for j in range(widend - 1, widstart, -1):
            res.append(matrix[j][lenstart])
        return lenstart + 1, lenend - 1, widstart + 1, widend - 1, res

    # AC_45%
    def printMatrix1(self, matrix):
        length = len(matrix) - 1
        width = len(matrix[0]) - 1
        res = []
        lenstart, widstart = 0, 0
        while length > lenstart and widstart < width:
            lenstart, length, widstart, width, tem = self.oneCircle(lenstart, length, widstart, width, matrix)
            res.extend(tem)
        else:
            if lenstart > length or widstart > width:
                pass
            elif length == lenstart:
                for j in range(widstart, width + 1):
                    res.append(matrix[lenstart][j])
            elif width == widstart:
                for i in range(lenstart, length + 1):
                    res.append(matrix[i][widstart])
        return res

    def oneCircle(self, lenstart, lenend, widstart, widend, matrix):
        res = []
        for i in range(lenstart, lenend + 1):
            res.append(matrix[widstart][i])
        if widstart < widend:
            for j in range(widstart + 1, widend + 1):
                res.append(matrix[j][lenend])
        else:
            return lenstart + 1, lenend - 1, widstart + 1, widend - 1, res
        if lenstart < lenend:
            for i in range(lenend - 1, lenstart - 1, -1):
                    res.append(matrix[widend][i])
        else:
            return lenstart + 1, lenend - 1, widstart + 1, widend - 1, res
        for j in range(widend - 1, widstart, -1):
            res.append(matrix[j][lenstart])
        return lenstart + 1, lenend - 1, widstart + 1, widend - 1, res

    def printMatrix(self, matrix):
        length = len(matrix) - 1
        width = len(matrix[0]) - 1
        res = []
        lenstart, widstart = 0, 0





if __name__ == '__main__':
    a = [[i for i in range(10)] for j in range(1)]
    print a
    s = Solution()
    res = s.printMatrix(a)
    print res
