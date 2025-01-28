    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_index] = nums[i]
                zero_index += 1
                
        for i in range(zero_index, len(nums)):
            nums[i]=0