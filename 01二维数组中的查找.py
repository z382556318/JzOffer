class Solution1:
    def Find(self, target, array):
        row = len(array) - 1
        column = len(array[0]) - 1
        i = 0
        j = column
        while i <= row and j >= 0:
            if target > array[i][j]:
                i += 1
            elif target < array[i][j]:
                j -= 1
            else:
                return True
        return False
class Solution2:
    def Find(self, target, array):
        # write code here
        n = len(array)
        flag = False
        for i in range(n):
            if target in array[i]:
                flag = True
                break
        return flag
while True:
    try:
        S = Solution2()
        L = list(eval(raw_input()))
        array = L[1]
        target = L[0]
        print(S.Find(target, array))
    except:
        break
if __name__ == '__main__':
    s = Solution1()
    s.Find(16,[[]])