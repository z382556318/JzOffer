# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def DoesTreeHasTree2(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        
        if pRoot2.val == pRoot1.val:
            return self.DoesTreeHasTree2(pRoot1.left, pRoot2.left) and self.DoesTreeHasTree2(pRoot1.right, pRoot2.right)
        else:
            return False


    def HasSubtree(self, pRoot1, pRoot2):
        flag = False
        if pRoot1 is not None and pRoot2 is not None:
            if pRoot1.val == pRoot2.val:
                flag = self.DoesTreeHasTree2(pRoot1, pRoot2)
            if not flag:
                flag = self.HasSubtree(pRoot1.left, pRoot2)
            if not flag:
                flag = self.HasSubtree(pRoot1.right, pRoot2)
            return flag




