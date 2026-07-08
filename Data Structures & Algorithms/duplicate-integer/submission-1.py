class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)):
            value = nums[i]
            # print(f"index: {i} value: {value}")
            for x in range(i+1, len(nums)):
                if(value == nums[x]):
                    count += 1
                # print(nums[x])
        if count > 0:
            return True
        else:
            return False