# -*- coding:utf-8 -*-
# 思路：迭代
# 测试样例：空链表
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode

    # 迭代：
    def Clone(self, pHead):
        if not pHead: return
        newcode = RandomListNode(pHead.label)
        newcode.random = pHead.random
        newcode.next = self.Clone(pHead.next)
        return newcode

    # 方法二
    def Clone(self, pHead):
        if not pHead: return

        # 步骤1：复制节点
        dummy = pHead
        while dummy:
            copynode = RandomListNode(dummy.label)
            dummynext = dummy.next
            dummy.next = copynode
            copynode.next = dummynext
            dummy = copynode.next

        # 步骤2：复制随机指针
        dummy = pHead
        while dummy:
            copynode = dummy.next
            if dummy.random:
                dummyrandom = dummy.random
                copynode.random = dummyrandom.next
            dummy = copynode.next

        # 步骤3：断开链表
        dummy = pHead
        copyhead = dummy.next
        copynode = copyhead
        while dummy:
            dummy.next = copynode.next
            dummy = dummy.next
            if dummy:
                copynode.next = dummy.next
                copynode = copynode.next
            else:
                copynode.next = None

        return copyhead

# 哈希表
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here

        head = pHead
        p_head = None
        new_head = None

        random_dic = {}
        old_new_dic = {}

        while head:
            node = RandomListNode(head.label)
            node.random = head.random
            old_new_dic[id(head)] = id(node)
            random_dic[id(node)] = node
            head = head.next

            if new_head:
                new_head.next = node
                new_head = new_head.next
            else:
                new_head = node
                p_head = node

        new_head = p_head
        while new_head:
            if new_head.random != None:
                new_head.random = random_dic[old_new_dic[id(new_head.random)]]
            new_head = new_head.next
        return p_head
