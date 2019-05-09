# -*- coding:utf-8 -*-
class DualLinkedList:
    def __init__(self, x = None):
        self.val = x
        self.pre = None
        self.after = None

class Solution:
    # 双向链表模拟——时间效率不高
    def LastRemaining_Solution(self, n, m):
        if n <= 0 or m <= 0: return -1
        if m == 1: return n - 1

        for i in range(n):
            if i == 0:
                pre_node = head = DualLinkedList(i)
                continue
            cur = DualLinkedList(i)
            pre_node.after = cur
            cur.pre = pre_node
            pre_node = cur

        head.pre = pre_node
        pre_node.after = head

        p = head
        while True:
            for i in range(m-1):
                p = p.after
            pre_node, after_node = p.pre, p.after
            if pre_node == after_node:
                return pre_node.val
            pre_node.after = after_node
            after_node.pre = pre_node
            p = after_node

if __name__ == '__main__':
    s = Solution()
    print s.LastRemaining_Solution(5,2)