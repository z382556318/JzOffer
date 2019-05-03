

class Solution:
    def FirstNotRepeatingChar(self, s):
        return s.index(list(filter(lambda c:s.count(c)==1,s))[0]) if s else -1


class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1

        di = {}

        for i in range(len(s)):
            if s[i] in di.keys():
                di[s[i]] = 10001
            else:
                di[s[i]] = i
        vals = sorted(di.values())
        print di
        return vals[0]

if __name__ == '__main__':
    s = Solution()
    print s.FirstNotRepeatingChar('google')