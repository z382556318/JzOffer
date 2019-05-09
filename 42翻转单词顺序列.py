# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        if len(s) == 1:return s
        return ' '.join(s.split()[::-1]) if s.strip() != "" else s

# 或者使用栈或两次翻转字符串
if __name__ == '__main__':
    a = 'i am a student'
    s = Solution()
    print s.ReverseSentence(a)