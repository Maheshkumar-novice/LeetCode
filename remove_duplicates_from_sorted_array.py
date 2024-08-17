# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_unique_element_index = 1
        previous_element = nums[0]
        for element in nums[1:]:
            if previous_element != element:
                nums[next_unique_element_index] = element
                next_unique_element_index += 1
            previous_element = element

        return next_unique_element_index
