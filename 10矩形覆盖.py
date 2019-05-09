
class Solution:
    def rectCover(self, number):
        if number <= 2:
            return number
        a, b = 1, 2
        for i in range(1,number):
            a, b = b, a + b
        return a