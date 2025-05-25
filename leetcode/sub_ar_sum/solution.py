# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Input: nums = [1,1,1], k = 2
# Output: 2

# Input: nums = [1,2,3], k = 3
# Output: 2


class Solution(object):

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum_count = {0: 1}  # Initialize with 0 sum to handle cases where subarray starts from index 0
        current_sum = 0
        sub_arrays = 0

        for num in nums:
            current_sum += num
            # Check if (current_sum - k) exists in the map
            if current_sum - k in prefix_sum_count:
                sub_arrays += prefix_sum_count[current_sum - k]
            # Update the prefix_sum_count map
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

        return sub_arrays