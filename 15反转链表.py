# -*- coding:utf-8 -*-
from listnode import *

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None
        elif pHead.next == None:
            return pHead
        p1, p2, p3 = pHead, pHead.next, pHead.next.next
        p1.next = None
        while True:
            p2.next = p1
            if p3 == None:
                break
            p1, p2, p3 = p2, p3, p3.next
        return p2

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        pre = None
        cur = pHead
        while cur != None:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre

#
# class Solution:
#     #  递归实现
#     def ReverseList(self, pHead):
#         if not pHead or not pHead.next:
#             return pHead
#         new_head = self.ReverseList(pHead.next)
#         pHead.next.next = pHead
#         pHead.next = None
#         return new_head

if __name__ == '__main__':
    ListNode_1 = ListNode_handle()
    l1 = ListNode()
    l1_list = [1, 8, 3]
    # l1_list = []
    for i in l1_list:
        l1 = ListNode_1.add(i)
    ListNode_1.print_ListNode(l1)
    print Solution().ReverseList(l1).val
