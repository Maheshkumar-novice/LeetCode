# https://leetcode.com/problems/sort-colors/description/
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Counting Sort
        book_keeper = [0, 0, 0]
        for num in nums:
            book_keeper[num] = book_keeper[num] + 1

        index = 0
        for i in range(3):
            for j in range(book_keeper[i]):
                nums[index] = i
                index += 1

        # index = 0
        # insert_index = 0
        # value = 0
        # while True:
        #     if insert_index == len(nums):
        #         break

        #     if index == 3 and value == 0:
        #         break

        #     if value == 0:
        #         value = book_keeper[index]
        #         index += 1
        
        #     if value == 0:
        #         continue

        #     nums[insert_index] = index - 1
        #     insert_index += 1
        #     value -= 1
