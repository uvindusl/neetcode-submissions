class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            value = nums[i]
            # print(f"index: {i} value: {value}")
            for x in range(i+1, len(nums)):
                if(value == nums[x]):
                    return True
                # print(nums[x])
        return False
