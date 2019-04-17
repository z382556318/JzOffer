# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd_list, even_lsit = [], []
        for i in range(len(array)):
            odd_list.append(array[i]) if array[i] % 2 == 1 else even_lsit.append(array[i])
        return odd_list + even_lsit

class Solution:
    def reOrderArray(self, array):
        return sorted(array,key = lambda c: c % 2, reverse=True)

class Solution:
    def reOrderArray(self, array):
        key = lambda c: c % 2
        for i in range(len(array)):
            if key(array[i]) == 1:
                j = i - 1
                tmp = array[i]
                while key(array[j]) == 0 and j >= 0:
                    array[j + 1] = array[j]
                    j = j - 1
                array[j + 1] = tmp
        return array

print Solution().reOrderArray([1,2,3,4,5,6,7])