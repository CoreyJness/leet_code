class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store the number and its index
        seen = {}
        for i, num in enumerate(nums):
            # Calculate the complement that would sum to the target
            complement = target - num
            # Check if the complement exists in the dictionary
            if complement in seen:
                return [seen[complement], i]
            # Store the current number with its index
            seen[num] = i
        return []