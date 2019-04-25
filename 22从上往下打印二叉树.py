# -*- coding:utf-8 -*-
# 思路:辅助队列：
# 若有左、右子树依次进队列，出队列的子树再次进队列，直至队列中无元素
# 测试样例：只有一个节点、斜树、空树

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root is None:
            return []

        queue = [root]
        result = []
        while queue:
            tmp = queue.pop(0)
            result.append(tmp.val)
            if tmp.left is not None:
                queue.append(tmp.left)
            if tmp.right is not None:
                queue.append(tmp.right)

        return result