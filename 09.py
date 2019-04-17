class Solution:

    def jumpFloorII(self, number):
        # write code here
        a = 1
        for i in range(1,number):
            a = 2 * a
        return a

class Solution:
    def jumpFloorII(self, number):
        if number < 0:
            return 0
        else:
            return pow(2, number - 1)

print Solution().jumpFloorII(3)