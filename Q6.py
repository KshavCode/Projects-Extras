class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr = list(set(nums))
        return len(arr) != len(nums)
