# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 暴力法
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 is None or pHead2 is None:
            return

        while pHead1:
            t = pHead2
            while t:
                if pHead1 == t:
                    return pHead1
                else:
                    t = t.next
            pHead1 = pHead1.next

        return None

class Solution:
    # 辅助栈
    # AC42——未分析完全相同情况
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 is None or pHead2 is None: return None

        stack1 = []
        stack2 = []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next

        if stack1[-1] != stack2[-1]:
            return None
        while stack1 and stack2:
            a = stack1.pop()
            b = stack2.pop()
            if a == b:
                tmp = a
            else:
                return tmp

        # 若两链表完全相同，无返回会报错：添加下列返回改正
        # return tmp
        # 或改为

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 is None or pHead2 is None: return None

        stack1 = []
        stack2 = []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next

        tmp = None
        while stack1 and stack2:
            a = stack1.pop()
            b = stack2.pop()
            if a == b:
                tmp = a
            else:
                break
        return tmp