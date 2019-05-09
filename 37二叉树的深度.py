# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归写法
    def TreeDepth(self, pRoot):
        if pRoot is None: return 0
        if pRoot.left is None and pRoot.right is None: return 1

        left_d = self.TreeDepth(pRoot.left)
        right_d = self.TreeDepth(pRoot.right)

        return 1 + max(left_d, right_d)

class Solution:
    # 非递归写法（用了栈:应该用队列）
    def TreeDepth(self, pRoot):
        if pRoot is None: return 0
        if pRoot.left is None and pRoot.right is None: return 1
        stack = []
        stack.append(pRoot)
        res = 1
        while True:
            tmp = []
            while stack:
                p = stack.pop()
                if p.left:
                    tmp.append(p.left)
                if p.right:
                    tmp.append(p.right)
            if not tmp:
                break
            res += 1
            stack.extend(tmp)
        return res


