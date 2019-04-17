# -*- coding:utf-8 -*-
# 思路：建立辅助栈和两个指针：
# 入栈，入栈指针后移：栈顶元素不等于出栈指针所指，循环至入栈；栈顶元素等于出栈指针则出栈，循环至栈顶元素判断；
# 测试样例：输入列表为空

class Solution:
    def IsPopOrder(self, pushV, popV):
        if len(pushV) == 0 or len(popV) == 0:
            return False

        stack = []
        p1 = 0
        p2 = 0

        while True:
            stack.append(pushV[p1])
            p1 += 1
            while stack and stack[-1] == popV[p2]:
                stack.pop()
                p2 += 1
            if len(stack) == 0 and p1 == len(pushV) and p2 == len(popV):
                return True
            elif p1 == len(pushV) and p2 != len(popV) and stack[-1] != popV[p2]:
                return False

if __name__ == '__main__':
    a = [1,2,3,4]
    b = [2,1,4,3]
    c = [4,2,3,1]
    s = Solution()
    print s.IsPopOrder(a,b)
    print s.IsPopOrder(a,c)
