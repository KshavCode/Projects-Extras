class Solution:
    def high(self, lis) :
        for i in range(2) :
            lis.remove(max(lis))
        return max(lis) 
        

    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3 :
            return max(nums)
        return self.high(nums)