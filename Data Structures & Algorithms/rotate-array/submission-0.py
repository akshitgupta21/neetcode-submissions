class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        nums[:]=list(nums[n-k:n])+list(nums[0:n-k])
        