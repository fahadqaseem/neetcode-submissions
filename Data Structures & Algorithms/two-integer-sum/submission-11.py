class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # Value --> index

        for i , n in enumerate(nums):
            dif = target - n
            if dif in seen:
                return [seen[dif],i]
            seen[n] = i