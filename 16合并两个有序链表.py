from listnode import *

class Solution:
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        if pHead1.val <= pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2

    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        result = ListNode(None)
        curnode = ListNode(None)

        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                if result.val is None:
                    result = curnode = pHead1
                else:
                    curnode.next = pHead1
                    curnode = curnode.next
                pHead1 = pHead1.next
            else:
                if result.val is None:
                    result = curnode = pHead2
                else:
                    curnode.next = pHead2
                    curnode = curnode.next
                pHead2 = pHead2.next
        else:
            if pHead1 is None:
                curnode.next = pHead2
            if pHead2 is None:
                curnode.next = pHead1
        return result


if __name__ == '__main__':
    ListNode_1 = ListNode_handle()
    l1 = ListNode()
    ListNode_2 = ListNode_handle()
    l2 = ListNode()
    l1_list = [5, 3, 1]
    l2_list = [6, 4, 2]
    for i in l1_list:
        l1 = ListNode_1.add(i)
    for j in l2_list:
        l2 = ListNode_2.add(j)
    # ListNode_1.print_ListNode(l1)
    # print '............................'
    # ListNode_2.print_ListNode(l2)
    # print '............................'
    print(ListNode_1.print_ListNode(Solution().Merge(l1, l2)))