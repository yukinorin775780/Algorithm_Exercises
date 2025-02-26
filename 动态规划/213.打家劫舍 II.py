class Solution:
    # 与打家劫舍类似，但分类讨论:
    # 1. 考虑头元素不考虑尾元素
    # 2. 不考虑头元素考虑尾元素
    # 3. 取两者最大值
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        result1 = self.robRange(nums, 0, len(nums) - 2)
        result2 = self.robRange(nums, 1, len(nums) - 1)
        return max(result1, result2)

    def robRange(self, nums: List[int], start:int, end:int) -> int:
        if end == start:
            return nums[start]
        
        prev_max = nums[start]
        curr_max = max(nums[start], nums[start + 1])

        for i in range(start + 2, end + 1):
            temp = curr_max
            curr_max = max(prev_max + nums[i], curr_max)
            prev_max = temp
        
        return curr_max
