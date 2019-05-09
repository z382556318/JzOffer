class Solution:
    def minNumberInRotateArray(self, rotateArray):
        return min(rotateArray)

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        for i in range(len(rotateArray)):
            if rotateArray[i] > rotateArray[i+1]:
                return rotateArray[i+1]

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        return sorted(rotateArray)[0]

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        i = 0
        j = len(rotateArray) - 1
        while j - i != 1:
            mid = int(i + round((j - i) / 2))
            if rotateArray[mid] >= rotateArray[i]:
                i = mid
            elif rotateArray[mid] <= rotateArray[j]:
                j = mid
        return rotateArray[j]

a = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
print(Solution().minNumberInRotateArray(a))