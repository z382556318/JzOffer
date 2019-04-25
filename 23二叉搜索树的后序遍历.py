# -*- coding:utf-8 -*-

# 思路：二叉搜索树
# 测试样例：空列表，一个元素列表，

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False

        if len(sequence) == 1:
            return True

        key = sequence[-1]
        i = -1
        j = len(sequence) - 1

        while sequence[i+1] < key:
            i += 1

        while sequence[j-1] > key:
            j -= 1

        if j == i + 1:
            if i >= 0:
                left = self.VerifySquenceOfBST(sequence[0:i+1])
            else:
                left = True
            if j < len(sequence) - 1:
                right = self.VerifySquenceOfBST(sequence[j:-1])
            else:
                right = True

            return left and right
        else:
            return False


if __name__ == '__main__':
    a = []
    s = Solution()
    print s.VerifySquenceOfBST(a)