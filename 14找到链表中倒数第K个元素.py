# -*- coding:utf-8 -*-
from listnode import *

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None:
            return None
        if k <= 0:
            return None
        p1, p2 = head, head
        for i in range(k - 1):
            p1 = p1.next
            if not p1:
                return None
        while p1.next != None:
            p1, p2 = p1.next, p2.next
        return p2

if __name__ == '__main__':
    ListNode_1 = ListNode_handle()
    l1 = ListNode()
    l1_list = [1, 8, 3, 21, 5, 4, 0]
    for i in l1_list:
        l1 = ListNode_1.add(i)
    print Solution().FindKthToTail(l1,8)
