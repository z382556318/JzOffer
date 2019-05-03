# -*- coding:utf-8 -*-
#

class Solution:
    # AC40（不是字典序列）
    def Permutation(self, ss):
        if len(ss) == 0:
            return []
        elif len(ss) == 1:
            return (ss,)
        l = len(ss)
        res = ()
        for i in range(l):
            head = ss[i]
            newss = ss[:i] + ss[i+1:]
            # 字符串的拼接
            partition = self.Permutation(newss)
            for j in partition:
                res = res + (head + j,)

        return tuple(set(res))

class Solution:
    def Permutation(self, ss):
        if len(ss) == 0:
            return []
        elif len(ss) == 1:
            return (ss,)
        l = len(ss)
        res = ()
        for i in range(l):
            head = ss[i]
            newss = ss[:i] + ss[i+1:]
            # 字符串的拼接
            partition = self.Permutation(newss)
            for j in partition:
                res = res + (head + j,)

        return sorted(tuple(set(res)))

import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        return sorted(list(set(map(''.join, itertools.permutations(ss)))))

if __name__ == '__main__':
    ss = 'asdad'
    s = Solution()
    print s.Permutation(ss)
