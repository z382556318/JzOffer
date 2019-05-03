# -*- coding:utf-8 -*-
# 思路：四个为一个周期（序号变化方式不同）
# 测试样例：空矩阵，一维矩阵
import random

class Solution:
    def oneCircle(self, lenstart, lenend, widstart, widend, matrix):
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
    def printMatrix(self, matrix):
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

# 测试样例：空矩阵，行矩阵，列矩阵，两行多列，多行两列

class Solution1:

    def printMatrix(self, matrix):
        if len(matrix) is None:
            return
        if len(matrix[0]) is None:
            return

        width_end = len(matrix) - 1
        length_end = len(matrix[0]) - 1
        width_start = 0
        length_start = 0
        res = []

        while True:
            for j in range(length_start, length_end + 1):
                res.append(matrix[width_start][j])

            if width_start == width_end:
                break
            else:
                width_start += 1

            for i in range(width_start, width_end + 1):
                res.append(matrix[i][length_end])

            if length_end == length_start:
                break
            else:
                length_end -= 1

            for j in range(length_end, length_start - 1, -1):
                res.append(matrix[width_end][j])

            if width_end == width_start:
                break
            else:
                width_end -= 1
            for i in range(width_end, width_start - 1, -1):
                res.append(matrix[i][length_start])

            if length_start == length_end:
                break
            else:
                length_start += 1

        return res



if __name__ == '__main__':
    a = [[i for i in range(10)] for j in range(1)]
    print a
    s = Solution1()
    res = s.printMatrix(a)
    print res
