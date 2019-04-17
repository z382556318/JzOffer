# -*- coding:utf-8 -*-
# 思路：指针排序
# 样例：出栈最小值怎么办？（次小值怎么保存）
# 样例：若有两个最小值怎么办

class Solution1:
    def __init__(self):
        self.stack = []
        self.sortlist = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        self.sortlist.append(len(self.stack) - 1)
        self.sortlist = sorted(self.sortlist,key=lambda x:self.stack[x])

    def pop(self):
        # write code here
        a = self.stack.pop()
        index = self.sortlist.index(len(self.stack))
        self.sortlist.pop(index)
        return a

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.stack[self.sortlist[0]]

# 辅助站存储最小值

class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minstack and self.minstack[-1] <= node:
            self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(node)

    def pop(self):
        # write code here
        a = self.stack.pop()
        self.minstack.pop()
        return a

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.minstack[-1]

if __name__ == '__main__':
    s = Solution()
    s.push(11)
    s.push(12)
    s.push(9)
    s.pop()
    s.push(1)
    s.push(0)
    s.pop()
    print s.min()
    s = []
    # if s:
    #     print 'a'
    # print