# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
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

    def IsBalanced_Solution(self, pRoot):
        # 重复计算了跟多节点深度
        if pRoot is None: return True

        left_d = self.TreeDepth(pRoot.left)
        right_d = self.TreeDepth(pRoot.right)

        if abs(left_d - right_d) <= 1:
            return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
        else:
            return False

class Solution:
    # 后序遍历——每个节点仅访问一次
    def IsBalanced_Solution(self, pRoot):
        return self.helper(pRoot) != -1

    def helper(self, root):
        if not root: return 0

        left = self.helper(root.left)
        if left == -1:
            return -1

        right = self.helper(root.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1