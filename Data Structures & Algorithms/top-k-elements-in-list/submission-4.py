class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        # print(count)
        values = list(dict(sorted(count.items(), key=lambda item: item[1])).keys())

        return values[-k:]



