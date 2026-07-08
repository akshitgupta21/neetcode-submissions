class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:       
        null_set=set()
        null_set.update(nums)
        if len(null_set)==len(nums):
            return False
        else:
            return True
a=Solution()
print(a.hasDuplicate([1,2,3,3]))

