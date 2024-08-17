# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        sum = nums[0]
        for i in range(1, len(nums)):
            sum = max(nums[i], sum + nums[i])
            best = max(best, sum)

        return best
