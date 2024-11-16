class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [x for x in range(len(nums)+1)]
        return sum(arr)-sum(nums)
                