# -*- coding:utf-8 -*-
# 思路：遍历二叉树的同时交换左右子树的值，直至节点为None
# 测试：空子树——返回

# 使用一个栈模拟递归调用

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Mirror(self, pRoot):
        if pRoot is None:
            return
        pRoot.left, pRoot.right = pRoot.right, pRoot.left
        self.Mirror(pRoot.left)
        self.Mirror(pRoot.right)

    def Mirror(self, pRoot):
        if pRoot is None:
            return None

        root = pRoot
        stack = []
        stack.append(root)

        while stack:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return root