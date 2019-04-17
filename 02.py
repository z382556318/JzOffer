# -*- coding:utf-8 -*-
class Solution:
    def replacespace(self,s):
        count = 0
        index = []
        for i in range(len(s)):
            if s[i] == ' ':
                count += 1
                index.append(i)
        # 从后往前替换
        s = s + '_' * 2 * count
        for j in range(len(s)-1,0-1,-1):
            if j not in index:
                s[j + count * 2] = s[j]
                # 运行错误，因为str无法改变
            else:
                count -= 1
                s[j] = '%'
                s[j + 1] = '2'
                s[j + 2] = '0'
        return s

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        count = 0
        index = []
        for i in range(len(s)):
            if s[i] == ' ':
                count += 1
                index.append(i)
        for j in range(len(index)-1,-1,-1):
            s = s[:index[j]] + '%20' + s[index[j]+1:]

        return s

class Solution():
    def replaceSpace(self,s):
        return s.replace(' ','%20')

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = list(s)
        count = len(s)
        for i in range(0,count):
            if s[i]==' ':
                s[i]='%20'
        return ''.join(s)

s = Solution()
print(s.replaceSpace("hello world!"))

