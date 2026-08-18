class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l ==1:
            return nums[0]
        if l == 2:
            return max(nums[0],nums[1])
        i = 2
        sol = [nums[0],max(nums[0],nums[1])]
        while i < l:
            sol.append(max(nums[i] + sol[i-2], sol[i-1]))
            i+=1
        return sol[-1]