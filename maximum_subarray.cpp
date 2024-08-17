// https://leetcode.com/problems/maximum-subarray/

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int a = nums[0];
        int b = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            a = std::max(nums[i], a + nums[i]);
            b = std::max(a, b);
        }
        return b;
    }
};
