class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 2:
            return number
        a = 1
        b = 2
        for i in range(1,number):
            a, b = b, a + b
        return a


print Solution().jumpFloor(3)
