class Solution1:
    def NumberOf1(self, n):
        # write code here
        return sum([(n >> i & 1) for i in range(0,32)])

class Solution2:
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            print bin(n)
            n = n & 0xffffffff
            print bin(n)
        while n:
            count += 1
            n = n & (n - 1)
        return count

class Solution3:
    def NumberOf1(self, n):
        count = 0
        while n:
            count += 1
            n = n & (n - 1)
        return count

class  Solution4:
    def NumberOf1(self, n):
        a = []
        for i in range(32):
            print bin(n)
            n = n >> i
            a.append(n & 1)
        return sum(a)

if __name__ == '__main__':
    print Solution4().NumberOf1(-1)