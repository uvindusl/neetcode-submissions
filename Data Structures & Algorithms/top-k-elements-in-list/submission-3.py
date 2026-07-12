class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        # print(count)
        values = list(dict(sorted(count.items(), key=lambda item: item[1])).keys())
        # values = list(count)
        # print(values)
        return values[-k:]



