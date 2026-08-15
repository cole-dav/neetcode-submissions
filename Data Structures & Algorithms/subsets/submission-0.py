class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        1,2,3
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                print(i , " return " , subset)
                return

            subset.append(nums[i])
            dfs(i+1)
            print(i , " pre " , subset)
            subset.pop()
            print(i , " pot1 " , subset)
            dfs(i+1)
            print(i , " pot2 " , subset)
        dfs(0)
        return res