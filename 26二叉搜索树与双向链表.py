# -*- coding:utf-8 -*-
# 思路：中序遍历存入队列
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        # 非递归
        if not pRootOfTree:
            return

        stack = []
        queue = []
        p = pRootOfTree
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                queue.append(p)
                p = p.right

        for i in range(len(queue)):
            if len(queue) == 1:
                return queue[0]
            if i == 0:
                queue[i].right = queue[i+1]
                continue
            if i == len(queue) - 1:
                queue[i].left = queue[i-1]
                break
            queue[i].left = queue[i-1]
            queue[i].right = queue[i+1]

        return queue[0]

class Solution1:
    def Convert(self, pRootOfTree):
        # 递归版本
        if not pRootOfTree:
            return
        if pRootOfTree.left is None and pRootOfTree.right is None:
            return pRootOfTree

        left = self.Convert(pRootOfTree.left)
        # left是链表头
        p = left

        while left and p.right:
            # 定位链表最右端节点(左子树链表最大值）
            p = p.right

        if left:
            p.right = pRootOfTree
            pRootOfTree.left = p

        right = self.Convert(pRootOfTree.right)

        if right:
            right.left = pRootOfTree
            pRootOfTree.right = right

        return left if left else pRootOfTree