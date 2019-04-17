# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre.pop(0))
        i = tin.index(root.val)
        # index（）函数
        root.left = self.reConstructBinaryTree(pre[:i], tin[:i])
        # 其实pre只传入前i即可
        root.right = self.reConstructBinaryTree(pre[i:], tin[i + 1:])
        return root


