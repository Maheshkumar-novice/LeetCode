# https://leetcode.com/problems/sort-an-array/

class Solution(object):
    def sortArray(self, nums):
        if len(nums) == 1:
            return nums

        mid_point = len(nums) // 2
        left = self.sortArray(nums[:mid_point])
        right = self.sortArray(nums[mid_point:])

        new_array = []
        i, j = 0, 0
        while i < len(left) and j < len(right):        
            if left[i] <= right[j]:
                new_array.append(left[i])
                i += 1
            else:
                new_array.append(right[j])
                j += 1

        return new_array + left[i:] + right[j:]
